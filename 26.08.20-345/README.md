## [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
- Input: s = "IceCreAm"
- Output: "AceCreIm"
- Explanation:
    
    The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
- Input: s = "leetcode"
- Output: "leotcede"

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consist of printable ASCII characters.

## 해석 및 풀이 방식
맨 앞에서 시작하는 포인터, 맨 뒤에서 시작하는 포인터를 둔 뒤 각각 vowels를 만나면 해당 위치의 값들을 바꿔주기.

그러고 두 포인터의 위치가 같아지거나 역전되면 끝내기

### 알고리즘
순차 탐색

### 시간복잡도: O(N)

### 공간복잡도:

## 다른사람들의 개쩌는답
