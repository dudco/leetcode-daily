## [3483. Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11)

**난이도:** 🟢 Easy

### 문제 설명
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

Example 1:
- Input: digits = [1,2,3,4]
- Output: 12
- Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.
Example 2:
- Input: digits = [0,2,2]
- Output: 2
- Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.
Example 3:
- Input: digits = [6,6,6]
- Output: 1
- Explanation: Only 666 can be formed.
Example 4:
- Input: digits = [1,3,5]
- Output: 0
- Explanation: No even 3-digit numbers can be formed.
Constraints:
- 3 <= digits.length <= 10
- 0 <= digits[i] <= 9

## 해석 및 풀이 방식
주어진 배열의 숫자들을 이용해서 짝수인 3자리숫자를 만드는 경우의 수

전부 다 확인해보면 될 것 같은데 마지막 숫자가 짝수일때만 확인하면됨

근데 이것만으로는 시간초과가 뜸 -> 맨 앞에 0이 못오게 막으면 통과함

### 알고리즘
- 브루트포스

### 시간복잡도: O(n^3)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
대부분 브루트포스로 해결. 근데 난 DFS 식으로 좀 복잡하게 한 느낌

그냥 for문 3개 중복으로 쓰는게 더 보기엔 편함

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        ans = 0

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[x]:
                        vis[x] = True
                        ans += 1

        return ans
```