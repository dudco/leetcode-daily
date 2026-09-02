## [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-28)

### 문제 설명
You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

Example 1:
- Input: s = "baba", target = "abba"
- Output: "baab"
- Explanation:

    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    
    The lexicographically smallest permutation that is strictly greater than target is "baab".

Example 2:
- Input: s = "baba", target = "bbaa"
- Output: ""
- Explanation:
    
    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Example 3:
- Input: s = "abc", target = "abb"
- Output: ""
- Explanation:
    
    s has no palindromic permutations. Therefore, the answer is "".

Example 4:
- Input: s = "aac", target = "abb"
- Output: "aca"
- Explanation:

    The only palindromic permutation of s is "aca".
    
    "aca" is strictly greater than target. Therefore, the answer is "aca".

Constraints:
- 1 <= n == s.length == target.length <= 300
- s and target consist of only lowercase English letters.

## 해석 및 풀이 방식
target 보다 큰 가장 작은 회문 순열을 만드는 문제.

1. 일단 source 문자열에있는 모든 문자 counting

2. target[i]와 같은 알파벳 선택 후 다음 target[i]로 이동

3. 만약 끝까지갔을 때 남은 알파벳이 target[i] 보다 작다면 빈 문자열 반환

4. 만약 끝까지갔을 때 남은 알파벳이 target[i] 보다 크다면 회문 순열인지확인 후 반환

5. 반환 된 후 다음것도 확인하는 방식으로 진행 / 해당 위치에서 target[i] 보다 큰 문자열이 나오면 남은 문자열로 회문을 구성할 수 있는지 처리 후 회문 구성이된다면 반환.

회문판별을 어떻게해야지 빠르게 가능할까?

### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
