## [3903. Smallest Stable Index I](https://leetcode.com/problems/smallest-stable-index-i/description/?envType=daily-question&envId=2026-09-04)

### 문제 설명
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

- max(nums[0..i]) is the largest value among the elements from index 0 to index i.
- min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.

Example 1:
- Input: nums = [5,0,1,4], k = 3
- Output: 3
- Explanation:

    - At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
    - At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
    - At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
    - At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
    - This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.

Example 2:
- Input: nums = [3,2,1], k = 1
- Output: -1
- Explanation:

    - At index 0, the instability score is 3 - 1 = 2.
    - At index 1, the instability score is 3 - 1 = 2.
    - At index 2, the instability score is 3 - 1 = 2.
    - None of these values is less than or equal to k = 1, so the answer is -1.

Example 3:
- Input: nums = [0], k = 0
- Output: 0
- Explanation:

    At index 0, the instability score is 0 - 0 = 0, which is less than or equal to k = 0. Therefore, the answer is 0.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9

## 해석 및 풀이 방식
단순 구현으로 풀어도 100개밖에 안되기때문에 상관없음. 

다만 max 값은 처음부터 시작하니 굳이 매 idx 마다 확인할필요는없고 앞에서부터 비교하면서 가장큰값을 도출해도 충분
### 알고리즘
- 단순구현

### 시간복잡도: O(N^2)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
min 값을 미리 계산해둔다면 O(N)의 시간으로도 가능함