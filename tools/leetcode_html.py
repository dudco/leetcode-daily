"""LeetCode 문제 HTML → 이 저장소 README 스타일 평문 변환기.

바꾸는 규칙 (기존 폴더들의 README.md 를 그대로 흉내낸다):
  <p>                     → 문단, 사이에 빈 줄
  <ul>/<ol>               → "- 항목"
  <pre>                   → Input/Output/Explanation 줄은 "- ", 나머지는 4칸 들여쓰기
  div.example-block       → 같은 규칙 + 설명 문단은 4칸 들여쓰기
  <sup>/<sub>             → ^ / _   (10<sup>5</sup> → 10^5)
  <code>/<strong>/<em>    → 태그만 제거, 글자는 그대로
  "Example 1:" "Constraints:" 뒤에는 빈 줄을 넣지 않는다
"""

import re
from html.parser import HTMLParser

VOID = {"br", "img", "hr", "input", "meta", "link", "source"}
TIGHT_HEAD = re.compile(r"^(Example\s*\d*\s*:|Constraints\s*:|Follow[- ]?up\s*:)\s*$", re.I)
IO_LINE = re.compile(r"^(Input|Output|Explanation)\s*:", re.I)


class Node:
    __slots__ = ("tag", "attrs", "children", "text")

    def __init__(self, tag, attrs=None, text=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []
        self.text = text


class _Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs))
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(Node("#text", text=data))


def _clean(s):
    s = s.replace(" ", " ").replace("​", "").replace("﻿", "")
    s = re.sub(r"[ \t]+", " ", s)
    return s


def inline(node):
    """블록 안의 글자만 뽑아낸다."""
    parts = []
    for c in node.children:
        if c.tag == "#text":
            parts.append(c.text)
        elif c.tag == "br":
            parts.append("\n")
        elif c.tag == "sup":
            parts.append("^" + inline(c))
        elif c.tag == "sub":
            parts.append("_" + inline(c))
        elif c.tag == "img":
            src = c.attrs.get("src", "")
            parts.append("![](%s)" % src if src else "")
        else:
            parts.append(inline(c))
    return _clean("".join(parts)).strip()


class Out:
    def __init__(self):
        self.lines = []
        self._tight = False

    def block(self, text, tight=False):
        text = text.rstrip()
        if not text.strip():
            return
        if self.lines and not self._tight:
            self.lines.append("")
        self.lines.extend(text.split("\n"))
        self._tight = tight

    def loosen(self):
        self._tight = False

    def value(self):
        return "\n".join(self.lines).strip("\n")


def _classes(node):
    return set((node.attrs.get("class") or "").split())


def _render_pre(node, out, indent=""):
    raw = inline(node)
    prev_io = False
    for line in raw.split("\n"):
        stripped = line.strip()
        if not stripped:
            prev_io = False
            continue
        if IO_LINE.match(stripped):
            out.block(indent + "- " + stripped, tight=True)
            prev_io = True
        elif prev_io:
            out.block(indent + "    " + stripped, tight=True)
        else:
            out.block(indent + stripped)
    out.loosen()  # <pre> 다음 블록 앞에는 빈 줄을 넣는다


def _render_list(node, out, indent=""):
    items = []
    for li in node.children:
        if li.tag != "li":
            continue
        txt = inline(li)
        if not txt:
            continue
        head, *rest = txt.split("\n")
        items.append(indent + "- " + head)
        items.extend(indent + "  " + r for r in rest)
    if items:
        out.block("\n".join(items))


def _render_para(node, out, in_example, indent=""):
    txt = inline(node)
    if not txt:
        return
    if TIGHT_HEAD.match(txt):
        out.block(indent + txt, tight=True)
        return
    if in_example:
        if IO_LINE.match(txt):
            # "Explanation:" 뒤에 문단이 이어지면 빈 줄을 둔다
            tight = not re.match(r"^Explanation\s*:\s*$", txt, re.I)
            out.block(indent + "- " + txt, tight=tight)
        else:
            body = "\n".join(indent + "    " + l for l in txt.split("\n"))
            out.block(body)
        return
    out.block("\n".join(indent + l for l in txt.split("\n")))


def _walk(node, out, in_example=False, indent=""):
    for c in node.children:
        if c.tag == "#text":
            if c.text.strip():
                out.block(_clean(c.text).strip())
        elif c.tag == "p":
            _render_para(c, out, in_example, indent)
        elif c.tag in ("ul", "ol"):
            _render_list(c, out, indent + ("    " if in_example else ""))
        elif c.tag == "pre":
            _render_pre(c, out, indent)
        elif c.tag in ("h1", "h2", "h3", "h4", "strong", "b"):
            txt = inline(c)
            if txt:
                out.block(indent + txt, tight=bool(TIGHT_HEAD.match(txt)))
        elif c.tag == "img":
            src = c.attrs.get("src", "")
            if src:
                out.block(indent + "![](%s)" % src)
        elif c.tag in ("div", "section", "blockquote", "span", "table", "tbody", "tr"):
            _walk(c, out, in_example or "example-block" in _classes(c), indent)
        else:
            _walk(c, out, in_example, indent)


def to_text(html):
    t = _Tree()
    t.feed(html or "")
    t.close()
    out = Out()
    _walk(t.root, out)
    text = out.value()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
