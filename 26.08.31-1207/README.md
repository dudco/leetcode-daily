## [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
- Input: arr = [1,2,2,1,1,3]
- Output: true
- Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
- Input: arr = [1,2]
- Output: false

Example 3:
- Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
- Output: true

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000
## 해석 및 풀이 방식
걍 해시맵으로 개수세고, set, len 이용해서 전부 다 유니크한지 확인

### 알고리즘
- 단순 구현
### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
