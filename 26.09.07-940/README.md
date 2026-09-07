## [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/description/?envType=daily-question&envId=2026-09-07)

### 문제 설명
Given a string s, return the number of distinct non-empty subsequences of s. 

Since the answer may be very large, return it modulo 10^9 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.)

Example 1:
- Input: s = "abc"
- Output: 7
- Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
- Input: s = "aba"
- Output: 6
- Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:
- Input: s = "aaa"
- Output: 3
- Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Example4:
- Input:s = "abcd"
- Output: 14
- Explanation "a", "b", "c", "d", "ab", "ac", "ad", "bc", "bd", "cd", "abc", "abd", "acd", "bcd", "abcd"

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters.
## 해석 및 풀이 방식
동일하게 DP로 풀면됨. DP 같은.. DFS랄까

암튼 i 번째 DP에는 i를 사용해서 만들 수 있는 개수임

dp[0] 은 s[0] 을 이용해서 만들 수 있는 최소 개수이므로 1

dp[1] 은 s[1] 까지의 문자들을 이용해 만들 수 있는 부분문자열 -> dp[0] 의 경우의 수 (1), s[1] 만 오는 경우 (1), s[1] 을 s[0]과 합치는 경우 (1)

==> dp[0] 에 s[1]을 더하는 경우의 수, s[1]만 이용하는 경우의 수 (dp[i-1]+1 + 1 = 3)

dp[2] 은 s[2] 까지의 문자들을 이용해 만들 수 있는 부분문자열 -> dp[1] 의 경우의 수 (dp[0]의 경우의 수가 이미 합쳐져있음 (3)), s[2]만 이용 (1), s[2]를 s[0]과 합치는 경우 (1), s[2]를 s[1]과 합치는경우 (1) 

==> dp[0] 에 s[2] 를 더하는 경우의 수, dp[1]에 s[2]를 더하는 경우의 수, s[2] 만 이용하는 경우의 수 (dp[i-1]+1 + dp[i-2]+1 + 1 = 7)

dp[3] 은 [s3] 까지의 문자들을 이용해 만들 수 있는 부분문자열

==> dp[i-1]+1 + dp[i-2]+1 + dp[i-3]+1 + 1 = 8+4+2+1

---

근데 이렇게 처리하면서 중복의 경우를 제외해야함. -> 어떻게하면될까?

1. chk 배열을 두고 i 번째 위치에서 해당 문자가 올 수 있는지 확인 
    
    ex1. chk[0][0] = False -> 맨앞에 a가 올 수 있음
    
    ex2. chk[1][1] = False -> 두번째에 b가 올 수 있음

2. 만약 i 번째 위치에 해당 문자가 이미 왔었다가 의미하는것은?

음 접근 자체가 잘못된거같은데

---

특정 문자 c가 첫번째에서만 존재할 수 있는가? -> chk[0][ord(c) - ord("a")]

특정 문자 c가 두번째에 오는데 s[j]의 뒤에 올 수 있는가? -> 앞의 문자가 뭐였는지 어떻게 기록하지? -> chk[1][]

l + e 는 이미했다 기록 / l + e + e 는 이미했다 기록 -> 이걸 어떻게 나타내지?

dp[0] = 1, ord(s[0]) - ord("a") 기록

만약 s[idx] "만" 쓴 기록이 이미 있음 -> dp[1] = 0 / 없음 -> dp[1] = 1

s[idx] 를 특정 문자열 뒤에 추가한다할 때 점화식은..? 

--- 

case1. "abc"

맨처음 "a"접근 -> "a" 가능 -> dp[0][0] = 1 # "a" 
                          dp[0][1] = 0
                          dp[0][2] = 0

두번째 "b"접근 -> "b" 가능 -> dp[1][0] = 1 # "b" 
                          dp[1][1] = 3 # (dp[0][0] + 1) + (dp[0][1] + 1) # ("a", "ab"), "b"
                          dp[1][2] = 0

세번재 "c"접근 -> "c" 가능 -> dp[2][0] = 1 # "c"
                          dp[2][1] = 3 # (dp[0][0] + 1) + (dp[0][1] + 1) # ("a", "ac"), "c"
                          dp[2][2] = 7 # (dp[1][0] + 1) + (dp[1][1] + 1) + (dp[1][2] + 1) # ("b", "bc"), ("a", "ab", "b", "abc"), "c"

---
포기: 
문자열의 각 문자를 앞에서부터 하나씩 확인하면서, 현재까지 만들 수 있는 서로 다른 부분 수열의 개수를 DP로 관리한다. 

어떤 문자 c를 새로 확인했을 때, 기존에 만들 수 있던 모든 부분 수열은 c를 선택하지 않는 경우와 선택해서 뒤에 붙이는 경우로 나뉜다. 

따라서 일단 경우의 수는 기존 개수의 두 배가 된다.

하지만 c가 이전에도 등장한 문자라면 중복이 생긴다. 

예를 들어 "lee"에서 두 번째 e를 처리할 때, 첫 번째 e를 붙여서 이미 만들었던 일부 문자열과 같은 결과가 다시 만들어진다. 

이 중복되는 개수는 c가 직전에 등장하기 전까지의 문자열로 만들 수 있었던 부분 수열 개수와 같다. 그래서 두 배로 늘린 값에서 해당 값을 빼 준다.

이를 위해 각 문자별로 마지막 등장 위치를 저장한다. 

dp[i]를 앞에서부터 i개 문자를 사용해 만들 수 있는 서로 다른 부분 수열의 개수라고 하면, 빈 문자열을 포함하기 위해 dp[0] = 1로 시작한다. 

현재 문자 c가 처음 등장했다면 dp[i] = 2 × dp[i-1]이고, 이전 등장 위치가 j라면 중복을 제거하여 dp[i] = 2 × dp[i-1] - dp[j-1]이 된다. 

모든 연산은 값이 커질 수 있으므로 매 단계마다 10^9 + 7로 나눈 나머지를 저장한다. 마지막에는 빈 문자열 하나를 제외하기 위해 dp[n] - 1을 반환한다.

### 알고리즘
- DP

### 시간복잡도: O(n)
문자열을 한 번만 순회하고 문자별 마지막 위치만 기록하므로 시간 복잡도는 O(n)이다.

### 공간복잡도: O(n)
DP 배열 저장을 위해 사이즈가 n인 배열이 필요하다.

## 다른사람들의 개쩌는답
