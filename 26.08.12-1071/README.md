## [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​

 

Constraints:

- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

## 해석 및 풀이 방식

### 알고리즘
그냥 두 문자열을 맨 앞부터 비교해가면서 처리하면 되지않나? -> 예외가 좀 어려울듯
1. 맨 앞에 한자리로만 전체가 이뤄져있는지 확인
2. 만약 그렇지않다면 다음자리로 이뤄져있는지 확인
3. 마지막까지 반복

### 시간복잡도: O(n)
최악의 경우 왼쪽포인터 O(n) + 오른쪽 포인터 O(n) 이므로 O(2n) -> O(n) 의 시간을 가짐

### 공간복잡도: O(n)
해시 테이블 데이터를 저장할 공간이 필요하니 O(n)의 공간복잡도를 가짐

## 다른사람들의 개쩌는답
거의 다 답이 비슷함. 근데 사람들은 C++로 풀어서 속도가 빠른듯. 