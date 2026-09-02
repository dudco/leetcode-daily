## [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
- Input: s = "the sky is blue"
- Output: "blue is sky the"

Example 2:
- Input: s = "  hello world  "
- Output: "world hello"
- Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
- Input: s = "a good   example"
- Output: "example good a"
- Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

## 해석 및 풀이 방식

앞에서부터 돌면서 큐에 넣고 pop 하는 방식 -> O(N)

양쪽에서부터 오면서 단어가 완성되면 배열에 넣고 재조합하는 방식 -> O(N/2)

### 알고리즘

### 시간복잡도: O(N)

### 공간복잡도: O(N)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/reverse-words-in-a-string/solutions/8464643/easy-approach-reverse-first-then-restore-f61p/?envType=study-plan-v2&envId=leetcode-75

조금 느리지만 간단한 코드. 그냥 split() 한 뒤 반대로 조합