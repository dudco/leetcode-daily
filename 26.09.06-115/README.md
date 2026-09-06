## [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/description/?envType=daily-question&envId=2026-09-06)

### 문제 설명
Given two strings s and t, return the number of distinct subsequencesofswhich equalst.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
- Input: s = "rabbbit", t = "rabbit"
- Output: 3
- Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from s.
    rabbbit
    rabbbit
    rabbbit

Example 2:
- Input: s = "babgbag", t = "bag"
- Output: 5
- Explanation:
    As shown below, there are 5 ways you can generate "bag" from s.
    babgbag
    babgbag
    babgbag
    babgbag
    babgbag

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.

## 해석 및 풀이 방식
dp[i][j] = s의 앞 i개 문자로 t의 앞 j개 문자를 만드는 방법의 수

s[i-1] != t[j-1]

→ 현재 s 문자를 버린다.

s[i-1] == t[j-1]

→ 현재 s 문자를 버리거나

→ 현재 s 문자를 사용하거나
### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
```
dp = [0] * (len(t) + 1)
dp[0] = 1

for c in s:
    for j in range(len(t), 0, -1):
        if c == t[j - 1]:
            dp[j] += dp[j - 1]

return dp[len(t)]
```

1차원 최적화도 가능