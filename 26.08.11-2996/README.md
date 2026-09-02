## [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/?envType=daily-question&envId=2026-08-11)

### 문제 설명
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]

Output: 6

Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:

Input: nums = [3,4,5,1,12,14,13]

Output: 15

Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50

1 <= nums[i] <= 50
## 해석 및 풀이 방식
증가하는 수열은 그냥 for문으로 처리하면 될 것 같음. for문 전체가 50개가 넘지 않으니까
그리고 구한 숫자에서 하나씩 더해가면서 가장 큰 항목을 찾으면 될듯. 전체 50이 안넘음.
이러면 단순 구현으로 O(n) 의 시간복잡도를 가지게됨.

### 알고리즘
단순구현

### 시간복잡도: O(n)
for문 두번도는거라 O(2n) -> O(n) 의 시간복잡도를 가짐

### 공간복잡도: O(1)
data를 담을 상수하나만 있으면되니 O(1)의 공간복잡도를 가짐

## 다른사람들의 개쩌는답
