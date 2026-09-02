## [3718. Smallest Missing Multiple of K](https://leetcode.com/problems/smallest-missing-multiple-of-k/description/?envType=daily-question&envId=2026-08-25)

### 문제 설명
Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.

A multiple of k is any positive integer divisible by k.

Example 1:
- Input: nums = [8,2,3,4,6], k = 2
- Output: 10
Explanation:

    The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

Example 2:
- Input: nums = [1,4,7,10,15], k = 5
- Output: 5
- Explanation:

    The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100

## 해석 및 풀이 방식
num 의 길이가 100밖에 안되어서 그냥 전체 탐색해도 되지만 해당 리스트를 set으로 변경 후 조회하는 로직을 이용하면 O(1)로 가능함

### 알고리즘
- set

### 시간복잡도: O(N)
set 으로 바꾸는 시간

### 공간복잡도: O(N)
set 저장할 공간

## 다른사람들의 개쩌는답
