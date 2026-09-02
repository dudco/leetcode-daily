## [3471. Find the Largest Almost Missing Integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/?envType=daily-question&envId=2026-08-18)

### 문제 설명
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:
- Input: nums = [3,9,2,1,7], k = 3
- Output: 7
- Explanation:
    - 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
    - 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
    - 3 appears in 1 subarray of size 3: [3, 9, 2].
    - 7 appears in 1 subarray of size 3: [2, 1, 7].
    - 9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
    - We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:
- Input: nums = [3,9,7,2,1,7], k = 4
- Output: 3
- Explanation:
    - 1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
    - 2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    - 3 appears in 1 subarray of size 4: [3, 9, 7, 2].
    - 7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    - 9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
    - We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:
- Input: nums = [0,0], k = 1
- Output: -1
- Explanation:
    - There is no integer that appears in only one subarray of size 1.

Constraints:
- 1 <= nums.length <= 50
- 0 <= nums[i] <= 50
- 1 <= k <= nums.length
## 해석 및 풀이 방식
1부터 증가시키면서 subarray 확인하는 방식? -> 너무 오래걸릴듯

Sliding Window로 돌면서 hash table을 채우고, 한번만 나온 가장 큰 숫자 찾기

### 알고리즘
거의 그냥 단순 구현이었음 Sliding Window라고 하지만 l, r 정해놓고 거기서 다시 돌면서 해시테이블 채운뒤 마지막에 전체를 다 돌면서 가장 올바른 값 찾기였음

중복 체크를 피하기위해 check 배열까지이용함

### 시간복잡도: O(N * K)
nums 길이 * K 의 길이 -> 만약 N과 K 가 50이상이라면 불가능할 알고리즘이었음

### 공간복잡도: O(N)
해시테이블을 위한 공간 + chk 배열 O(50) 

## 다른사람들의 개쩌는답
https://leetcode.com/problems/find-the-largest-almost-missing-integer/solutions/8467083/beats-100-easy-beginner-friendly-code-ha-c420/?envType=daily-question&envId=2026-08-18

k == 1 이면 전부 다 subarray -> nums 배열에서 한번만 등장하는 숫자 중 가장 큰 숫자를 반환하면됨

k == n 이면 subarray가 하나뿐 -> nums 배열에서 가장 큰 숫자 아무거나 반환하면됨

1 < k < n 이면 한번만 등장할 수 있는 숫자는 맨앞 또는 맨뒤 뿐임 -> 맨앞과 맨뒤 숫자중 한번도 등장하지 않으면서 더 큰 숫자 반환하면됨

이렇게하면 O(N) 으로 가능