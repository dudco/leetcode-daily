## [338. Counting Bits](https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).

Example 1:
- Input: n = 2
- Output: [0,1,1]
- Explanation:
    - 0 --> 0
    - 1 --> 1
    - 2 --> 10

Example 2:
- Input: n = 5
- Output: [0,1,1,2,1,2]
- Explanation:
    - 0 --> 0
    - 1 --> 1
    - 2 --> 10
    - 3 --> 11
    - 4 --> 100
    - 5 --> 101

Constraints:
- 0 <= n <= 10^5 

Follow up:
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?

## 해석 및 풀이 방식
비트연산으로 가장 마지막 비트가 1인지 확인 후 1이면 + 1

그러고 비트를 한자리 오른쪽으로 옮김
### 알고리즘

### 시간복잡도: O(n log n)

바깥 반복문이 0부터 n까지 총 n + 1번 돌고, 각 idx마다 이진수의 비트 수만큼 while이 반복됨. 가장 큰 수 n의 비트 수는 약 log₂n 임

### 공간복잡도: O(n)

## 다른사람들의 개쩌는답
지피티가 알려줌: ret[i] = ret[i >> 1] + (i & 1)

위 점화식을 이용하면 O(n) 으로 가능함. i번째 숫자 비트의 1의 개수는 i의 맨 왼쪽 비트 제거 후 i의 맨 오른쪽이 1인지 확인하면됨

외에도 다양한 점화식으로 가능함