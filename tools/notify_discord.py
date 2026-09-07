#!/usr/bin/env python3
"""새로 생성한 LeetCode 데일리 문제를 Discord Webhook으로 알린다."""

import json
import os
import sys
import time
import urllib.error
import urllib.request


COLORS = {
    "Easy": 0x00B8A3,
    "Medium": 0xFFC01E,
    "Hard": 0xFF375F,
}


def build_payload(env):
    difficulty = env.get("LEETCODE_DIFFICULTY", "Unknown")
    problem_id = env.get("LEETCODE_PROBLEM_ID", "")
    title = env.get("LEETCODE_TITLE", "오늘의 문제")
    display_title = "%s. %s" % (problem_id, title) if problem_id else title

    payload = {
        "username": "LeetCode Daily",
        "allowed_mentions": {"parse": []},
        "embeds": [{
            "title": display_title,
            "url": env["LEETCODE_PROBLEM_URL"],
            "description": "오늘의 LeetCode 문제 초안이 생성되었습니다.",
            "color": COLORS.get(difficulty, 0x5865F2),
            "fields": [
                {"name": "난이도", "value": difficulty, "inline": True},
                {"name": "폴더", "value": "`%s`" % env["LEETCODE_FOLDER"],
                 "inline": True},
            ],
            "footer": {"text": env.get("GITHUB_REPOSITORY", "GitHub Actions")},
        }],
    }
    commit_url = env.get("LEETCODE_COMMIT_URL")
    if commit_url:
        payload["embeds"][0]["fields"].append({
            "name": "GitHub",
            "value": "[생성된 커밋 보기](%s)" % commit_url,
            "inline": False,
        })
    return payload


def send(webhook_url, payload, tries=3):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    last_error = None
    for attempt in range(1, tries + 1):
        try:
            request = urllib.request.Request(
                webhook_url,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "leetcode-daily-github-action/1.0",
                },
            )
            with urllib.request.urlopen(request, timeout=20) as response:
                if response.status not in (200, 204):
                    raise RuntimeError("예상하지 못한 HTTP 상태: %s" % response.status)
            return
        except (urllib.error.URLError, RuntimeError) as error:
            last_error = error
            if attempt < tries:
                print("Discord 전송 실패(%d/%d), 재시도합니다." % (attempt, tries),
                      file=sys.stderr)
                time.sleep(attempt * 2)
    raise SystemExit("Discord 알림 전송 실패: %s" % last_error)


def main():
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        raise SystemExit("DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")
    send(webhook_url, build_payload(os.environ))
    print("Discord 알림을 전송했습니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
