## [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
- Input: nums = [0,1,0,3,12]
- Output: [1,3,12,0,0]

Example 2:
- Input: nums = [0]
- Output: [0]
 

Constraints:
1 <= nums.length <= 10^4
-231 <= nums[i] <= 231 - 1

## 해석 및 풀이 방식
대표적인 투포인터 문제.

배열을 순회, 0이 아닌 값을 만나면 l이랑 바꿔주고 l++ 해주면됨

### 알고리즘

### 시간복잡도: 

### 공간복잡도: 

## 다른사람들의 개쩌는답
거의 다 답이 비슷함. 근데 사람들은 C++로 풀어서 속도가 빠른듯. 