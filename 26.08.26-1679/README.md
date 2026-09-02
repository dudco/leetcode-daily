## [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
- Input: nums = [1,2,3,4], k = 5
- Output: 2
- Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    
    There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
- Input: nums = [3,1,3,4,3], k = 6
- Output: 1
- Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    
    There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9

## 해석 및 풀이 방식
정렬 후 양쪽값을 더해봄 
1. 해당 값이 k 보다 작으면 l 증가, 크면 r 감소
2. 만약 k와 같아진다면 l, r 에 있는 요소를 제거 후 l += 1, r -= 1

### 알고리즘
- Two pointer

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
