## [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
- Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
- Output: 6
- Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
- Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
- Output: 10
- Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

## 해석 및 풀이 방식
주어진 배열에서 0을 k개 만큼 1로 바꿀 수 있을 때 연속적으로 나타나는 1의 개수는 최대 몇개안지 물어보는 문제

left, right 부터 시작 만약 right가 0이면 flip, 해당 위치를 기록해둠, right는 계속증가하다가 만약 더이상 flip 이 불가하면 그 때 부터 left 증가

left가 증가하다가 flip했던 위치에 도달하면 left 증가 후 flip 기록 제거

다시 right 증가

어케하지?

One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!

Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?

We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).

The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.


### 알고리즘
- sliding windows

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
