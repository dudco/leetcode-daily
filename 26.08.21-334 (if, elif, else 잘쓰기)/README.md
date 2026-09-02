## [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
- Input: nums = [1,2,3,4,5]
- Output: true
- Explanation: Any triplet where i < j < k is valid.

Example 2:
- Input: nums = [5,4,3,2,1]
- Output: false
- Explanation: No triplet exists.

Example 3:
- Input: nums = [2,1,5,0,4,6]
- Output: true
- Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 
Constraints:
- 1 <= nums.length <= 5 * 10^5
- -231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
 
## 해석 및 풀이 방식
어떻게 접근해야하지?

if, elif, else를 잘쓰면 쉽게 해결되는 문재였슨;;

하 간단한것도 못풀다니 한심슨

### 알고리즘
그냥 앞에서부터 쭉 도는것

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
