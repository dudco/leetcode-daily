## [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
- Input: nums = [1,2,3,4]
- Output: [24,12,8,6]

Example 2:
- Input: nums = [-1,1,0,-3,3]
- Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
## 해석 및 풀이 방식
자기 자신을 제외한 나머지 array 값들에 곱해주기 -> O(N^2)이 되어버림

Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?

Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

결과 배열의 idx 기준 왼쪽 누적곱을 먼저 구해주고 추가적으로 오른쪽 누적곱을 해당 배열에 곱해주면 O(2*N) 으로 가능

### 알고리즘
순차 탐색

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
