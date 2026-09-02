## [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
- Input: s = "abc", t = "ahbgdc"
- Output: true

Example 2:
- Input: s = "axc", t = "ahbgdc"
- Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

## 해석 및 풀이 방식
앞에서부터 같은 애가나오면 그냥 다음걸로 넘어가서 확인해보면됨.

Fllow up -> 주어지는 s의 개수가 많아진다면 일일이 확인하는건 별로임. -> next occurance 테이블을 미리 만들고 해당 테이블로부터 조회하도록 처리

### 알고리즘

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
