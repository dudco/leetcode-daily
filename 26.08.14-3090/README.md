## [3090. Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=daily-question&envId=2026-08-14)

### 문제 설명
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

Example 1:
- Input: s = "bcbbbcba"
- Output: 4
- Explanation:

    The following substring has a length of 4 and contains at most two occurrences of each character: "bcba".

Example 2:
- Input: s = "aaaa"
- Output: 2
- Explanation:
    
    The following substring has a length of 2 and contains at most two occurrences of each character: "aa".
 

Constraints:
- 2 <= s.length <= 100
- s consists only of lowercase English letters.

## 해석 및 풀이 방식
문자열의 길이가 그리 길진 않음

sliding window로 처리하면 100회 이내에 처리가 가능하긴함.

왼쪽, 오른쪽 포인터를 두고 오른쪽 포인터를 오른쪽으로 옮겨가면서 문자열의 개수를 셈. 

만약 특정 문자가 2개 이상이면 왼쪽 포인터를 오른쪽으로 올김

오른쪽 포인터가 가르키는 숫자에는 cnt + 1, 왼쪽 포인터가 가르키는 숫자에는 cnt - 1

### 알고리즘
- Sliding Window
- Hash Table

### 시간복잡도: O(n)

### 공간복잡도: O(1)
저장하는 문자가 소문자 26자 고정이기때문에 공간복잡도는 O(1)

## 다른사람들의 개쩌는답
