# LeetCode 데일리

매일 아침 LeetCode 데일리 문제 폴더가 자동으로 하나 생긴다.
푸는 건 내가 한다. 자동화는 **문제를 옮겨 적는 일까지만** 한다.

## 폴더 하나에 들어가는 것

```
26.09.02-3875/
├── README.md    링크 · 영문 원문 · 내가 채울 빈 칸
├── solution.py  LeetCode가 주는 시그니처만 (본문은 pass)
└── test.py      문제에 적힌 Example 케이스만
```

`README.md`에서 자동으로 채워지는 건 제목·링크·난이도·`### 문제 설명` 까지다.
그 아래 `## 해석 및 풀이 방식`, `### 알고리즘`, `### 시간복잡도:`,
`### 공간복잡도:`, `## 다른사람들의 개쩌는답` 은 빈 칸으로 남는다.

## 일부러 안 넣는 것

- **접근법·풀이·의사코드** — 그걸 생각하는 게 목적이니까
- **토픽 태그와 힌트** — API로 받을 수는 있지만 "이건 DP다" 한 줄이
  문제의 절반을 날린다. 풀고 나서 `### 알고리즘` 칸에 직접 적는다.
- **한글 번역·요약** — 영어로 읽는 게 목적의 나머지 절반

## 직접 돌리기

```bash
python3 tools/new_daily.py                 # 오늘 데일리
python3 tools/new_daily.py --force         # 폴더가 있어도 덮어씀
python3 tools/new_daily.py --slug two-sum  # 특정 문제
```

이미 그날 폴더가 있으면 건드리지 않는다. 폴더 이름에
`(세그먼트 트리) Hard` 같은 꼬리표를 붙여둬도 같은 문제로 알아본다.

## 자동 실행

`.github/workflows/daily-draft.yml` 이 09:07 KST에 돈다. GitHub 예약 실행은 정시를 잘
안 지키고 회차를 건너뛰기도 해서 10:38, 13:23 KST에도 한 번씩 더 건다.
그날 폴더가 이미 있으면 아무것도 하지 않으므로 중복 걱정은 없다.
LeetCode가 러너 IP를 막아 실패하는 날이 있을 수 있어서 5번까지 재시도한다.
그래도 실패하면 Actions 탭에서 "Run workflow"를 누르거나 로컬에서 돌리면 된다.

### Discord 알림 설정

새 문제를 커밋하고 GitHub에 푸시한 뒤 Discord 채널로 제목, 난이도, 문제 링크,
생성된 커밋 링크를 보낸다. Discord Bot이나 API Token은 필요 없고, 채널 전용
Webhook URL 하나만 있으면 된다.

1. Discord 서버에서 **서버 설정 → 연동(Integrations) → 웹후크(Webhooks) → 새 웹후크**로 이동한다.
2. 알림을 받을 채널을 선택하고 **웹후크 URL 복사**를 누른다.
3. GitHub 저장소에서 **Settings → Secrets and variables → Actions → New repository secret**으로 이동한다.
4. 이름은 `DISCORD_WEBHOOK_URL`, 값은 복사한 전체 Webhook URL로 저장한다.
5. **Actions → daily draft → Run workflow**로 수동 실행해 알림을 확인한다. 단, 오늘 폴더가 이미 있으면 중복 생성을 막기 위해 알림도 보내지 않는다.

Webhook URL은 해당 채널에 메시지를 보낼 수 있는 비밀 자격 증명이다. `.env`, 코드,
README 또는 Actions 로그에 직접 넣지 말고 GitHub Secret에만 저장한다. URL이 유출되면
Discord에서 해당 Webhook을 삭제하고 새로 만들어 Secret 값을 교체한다.

> 예약 실행은 저장소에 60일간 아무 활동이 없으면 GitHub가 꺼버린다.
> 매일 커밋이 쌓이는 한 그럴 일은 없다.

## 테스트 돌리기

VS Code에서 `test.py`를 열고 실행 구성 "Run test.py in current file folder".
터미널이면 문제 폴더 안에서 `python3 -B -m unittest test`.
