## [1621. Number of Sets of K Non-Overlapping Line Segments](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/?envType=daily-question&envId=2026-09-16)

**난이도:** 🟡 Medium

### 문제 설명
Given n points on a 1-D plane, where the i^th point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 10^9 + 7.

Example 1:
![](https://assets.leetcode.com/uploads/2020/09/07/ex1.png)

- Input: n = 4, k = 2
- Output: 5
- Explanation: The two line segments are shown in red and blue.
    The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

Example 2:
- Input: n = 3, k = 1
- Output: 3
- Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

Example 3:
- Input: n = 30, k = 7
- Output: 796297179
- Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10^9 + 7 gives us 796297179.

Constraints:
- 2 <= n <= 1000
- 1 <= k <= n-1

## 해석 및 풀이 방식
n개의 점이있는 1차원 평면에서 선 k를 그릴 때 안겹치도록 그려지는 개수는? k는 n보다 작음

점i까지에 대해서 j개의 구간을 만든다고할 때 

-> 만약 해당 i가 어떤 구간의 끝점이다? end[i][j]

-> 만약 해당 i가 어떤 구간의 끝점이 아니다? notEnd[i][j]

점화식
1) 만약 새롭게 확인하는 i가 어떤 구간의 끝점이라면?
1-1) i-1 이 끝점이었던 구간을 연장 -> end[i][j] = end[i-1][j]
1-2) i-1, i로 새로운 구간 생성 -> end[i][j+1] = end[i-1][j] + 1
2) 만약 새롭게 확인하는 i가 어떤 구간의 끝점이 아니라면? -> 이전 점까지만 사용한것
2-1) notEnd[i][j] = end[i-1][j]

초기값: end[1][1] = 1 / notEnd[1][1] = 0
둘째값: end[2][1] = 2, end[2][2] = 1 / notEnd[2][1] = 1, notEnd[2][2] = 0
셋째값: end[3][1] = 

### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
