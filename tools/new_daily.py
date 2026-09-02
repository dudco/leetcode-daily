#!/usr/bin/env python3
"""LeetCode 데일리 문제 초안 생성기.

만드는 것 — `YY.MM.DD-<문제번호>/` 폴더 하나와 그 안의 세 파일:
  README.md    문제 링크 + 영문 원문 + 내가 채워야 할 빈 칸
  solution.py  LeetCode가 주는 python3 시그니처만 (본문은 pass)
  test.py      문제에 적힌 Example 케이스만 옮긴 unittest

일부러 만들지 않는 것 — 접근법, 알고리즘 이름, 토픽 태그, 힌트, 풀이 코드.
토픽 태그와 힌트는 API로 받을 수는 있지만 그 자체가 스포일러라 받지 않는다.
`### 알고리즘` 칸은 문제를 푼 뒤 직접 채우는 자리다.

사용법
  python3 tools/new_daily.py                # 오늘 데일리
  python3 tools/new_daily.py --force        # 폴더가 이미 있어도 덮어씀
  python3 tools/new_daily.py --slug two-sum # 특정 문제로
  python3 tools/new_daily.py --dump-json a.json   # 받은 원본 저장 (디버그)
  python3 tools/new_daily.py --from-json a.json   # 네트워크 없이 재생성 (디버그)
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from leetcode_html import to_text  # noqa: E402

ENDPOINT = "https://leetcode.com/graphql/"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ),
    "Referer": "https://leetcode.com/problemset/all/",
    "Origin": "https://leetcode.com",
}

Q_DAILY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question { questionFrontendId title titleSlug difficulty }
  }
}
"""

# topicTags / hints 는 일부러 요청하지 않는다 (스포일러)
Q_DETAIL = """
query questionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    metaData
    exampleTestcases
    codeSnippets { langSlug code }
  }
}
"""


def gql(query, variables=None, tries=5):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(ENDPOINT, data=payload, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                body = json.loads(r.read().decode("utf-8"))
            if body.get("errors"):
                raise RuntimeError("GraphQL 오류: %s" % body["errors"])
            return body["data"]
        except Exception as e:  # noqa: BLE001
            last = e
            wait = 3 * (i + 1)
            print("  요청 실패(%d/%d): %s — %d초 뒤 재시도" % (i + 1, tries, e, wait),
                  file=sys.stderr)
            time.sleep(wait)
    raise SystemExit("LeetCode API 호출 실패: %s" % last)


# --------------------------------------------------------------------------- #
# solution.py

TYPING_FIX = [
    (re.compile(r"\bList\["), "list["),
    (re.compile(r"\bDict\["), "dict["),
    (re.compile(r"\bTuple\["), "tuple["),
    (re.compile(r"\bSet\["), "set["),
    (re.compile(r"\bOptional\[([^\[\]]+)\]"), r"\1 | None"),
]


def build_solution(detail):
    code = ""
    for s in detail.get("codeSnippets") or []:
        if s.get("langSlug") == "python3":
            code = s.get("code") or ""
            break
    if not code:
        name = json.loads(detail.get("metaData") or "{}").get("name", "solve")
        code = "class Solution:\n    def %s(self):\n" % name
    for pat, rep in TYPING_FIX:
        code = pat.sub(rep, code)
    lines = [l.rstrip() for l in code.rstrip().split("\n")]
    # 시그니처만 오고 본문이 비어 있으면 import 가 되도록 pass 를 채운다
    last = lines[-1] if lines else ""
    if last.lstrip().startswith("def ") or not last.strip():
        while lines and not lines[-1].strip():
            lines.pop()
        indent = len(lines[-1]) - len(lines[-1].lstrip()) if lines else 4
        lines.append(" " * (indent + 4) + "pass")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# test.py

def py_lit(raw):
    """LeetCode 의 JSON 값 문자열을 파이썬 리터럴 문자열로."""
    try:
        v = json.loads(raw)
    except Exception:  # noqa: BLE001
        return None
    return _fmt(v)


def _fmt(v):
    if v is True:
        return "True"
    if v is False:
        return "False"
    if v is None:
        return "None"
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        return "[" + ", ".join(_fmt(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join("%s: %s" % (_fmt(k), _fmt(x)) for k, x in v.items()) + "}"
    return repr(v)


TEST_HEAD = """import unittest

import solution


class SolutionTests(unittest.TestCase):
"""
TEST_TAIL = """
if __name__ == '__main__':
    unittest.main()
"""


def build_test(detail, body_md):
    meta = json.loads(detail.get("metaData") or "{}")
    fn = meta.get("name") or "solve"
    params = meta.get("params") or []
    ret = (meta.get("return") or {}).get("type", "")
    nparam = len(params) or 1

    raw_inputs = [l for l in (detail.get("exampleTestcases") or "").split("\n")]
    raw_inputs = [l for l in raw_inputs if l.strip() != ""] if any(
        l.strip() for l in raw_inputs) else []
    cases_in = [raw_inputs[i:i + nparam] for i in range(0, len(raw_inputs), nparam)]
    cases_in = [c for c in cases_in if len(c) == nparam]

    outs = re.findall(r"^- Output:\s*(.*)$", body_md, re.M)

    needs_node = any(
        t in (p.get("type") or "") for p in params for t in ("ListNode", "TreeNode"))

    notes = []
    lines = []
    if not cases_in or len(outs) < len(cases_in):
        notes.append("    # 예시 케이스를 자동으로 옮기지 못했다. 문제를 보고 직접 채울 것.")
    if needs_node:
        notes.append("    # 입력이 ListNode/TreeNode 다. 아래 리스트를 노드로 바꾸는")
        notes.append("    #   헬퍼를 직접 만든 뒤 주석을 풀 것.")

    n = min(len(cases_in), len(outs))
    for i in range(n):
        args = [py_lit(x) for x in cases_in[i]]
        exp = py_lit(outs[i].strip())
        if any(a is None for a in args) or exp is None:
            lines.append("    # def test_case%d(self):   # 값 해석 실패, 직접 옮길 것" % (i + 1))
            lines.append("    #     s = solution.Solution()")
            lines.append("    #     self.assertEqual(s.%s(%s), %s)"
                         % (fn, ", ".join(x.strip() for x in cases_in[i]), outs[i].strip()))
            lines.append("")
            continue
        call = "s.%s(%s)" % (fn, ", ".join(args))
        assertion = ("self.assertAlmostEqual(%s, %s, places=5)" % (call, exp)
                     if ret in ("double", "float") else
                     "self.assertEqual(%s, %s)" % (call, exp))
        mark = "    # " if needs_node else "    "
        lines.append("%sdef test_case%d(self):" % (mark, i + 1))
        lines.append("%s    s = solution.Solution()" % mark)
        lines.append("%s    %s" % (mark, assertion))
        lines.append("")

    if not lines:
        lines = [
            "    def test_case1(self):",
            "        s = solution.Solution()",
            "        self.assertEqual(s.%s(), None)  # TODO" % fn,
            "",
        ]
    body = "\n".join(notes + ([""] if notes else []) + lines).rstrip() + "\n"
    return TEST_HEAD + body + TEST_TAIL


# --------------------------------------------------------------------------- #
# README.md

README_TMPL = """## [{fid}. {title}]({link})

### 문제 설명
{body}

## 해석 및 풀이 방식

### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
"""


def build_readme(detail, date, body_md):
    link = ("https://leetcode.com/problems/%s/description/"
            "?envType=daily-question&envId=%s" % (detail["titleSlug"], date))
    return README_TMPL.format(
        fid=detail["questionFrontendId"], title=detail["title"],
        link=link, body=body_md)


# --------------------------------------------------------------------------- #

def folder_name(date, fid):
    y, m, d = date.split("-")
    return "%s.%s.%s-%s" % (y[2:], m, d, fid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (폴더 이름용, 기본은 데일리 날짜)")
    ap.add_argument("--slug", help="데일리 대신 특정 문제 슬러그")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--force", action="store_true", help="이미 있어도 덮어씀")
    ap.add_argument("--dump-json", help="받은 원본 JSON 저장")
    ap.add_argument("--from-json", help="네트워크 대신 저장해둔 JSON 사용")
    args = ap.parse_args()

    if args.from_json:
        blob = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
        date, detail = blob["date"], blob["detail"]
    else:
        if args.slug:
            slug = args.slug
            date = args.date or time.strftime("%Y-%m-%d", time.gmtime())
        else:
            daily = gql(Q_DAILY)["activeDailyCodingChallengeQuestion"]
            slug = daily["question"]["titleSlug"]
            date = args.date or daily["date"]
        detail = gql(Q_DETAIL, {"titleSlug": slug})["question"]
        if not detail:
            raise SystemExit("문제를 찾지 못했다: %s" % slug)

    if args.date:
        date = args.date
    if args.dump_json:
        Path(args.dump_json).write_text(
            json.dumps({"date": date, "detail": detail}, ensure_ascii=False, indent=2),
            encoding="utf-8")

    root = Path(args.root)
    name = folder_name(date, detail["questionFrontendId"])

    # 폴더 이름에 "(메모) Hard" 같은 꼬리가 붙어 있어도 같은 문제로 본다
    existing = [p for p in root.glob(name + "*") if p.is_dir()]
    if existing and not args.force:
        print("이미 있음: %s — 건너뜀" % existing[0].name)
        _emit_output(created="", folder=existing[0].name, skipped="1")
        return 0

    target = existing[0] if existing else root / name
    target.mkdir(parents=True, exist_ok=True)

    body_md = to_text(detail.get("content") or "")
    files = {
        "README.md": build_readme(detail, date, body_md),
        "solution.py": build_solution(detail),
        "test.py": build_test(detail, body_md),
    }
    for fname, text in files.items():
        path = target / fname
        if path.exists() and not args.force:
            print("  건너뜀 %s (이미 있음)" % fname)
            continue
        path.write_text(text, encoding="utf-8")
        print("  씀    %s" % fname)

    print("만듦: %s  (%s)" % (target.name, detail.get("difficulty", "")))
    _emit_output(created="1", folder=target.name, skipped="")
    return 0


def _emit_output(**kw):
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as f:
        for k, v in kw.items():
            f.write("%s=%s\n" % (k, v))


if __name__ == "__main__":
    raise SystemExit(main())
