## [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-14)

**난이도:** 🟢 Easy

### 문제 설명
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return trueif they overlap, otherwise returnfalse.

Example 1:
- Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
- Output: true

Example 2:
- Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
- Output: false

Example 3:
- Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
- Output: false

Constraints:
- rec1.length == 4
- rec2.length == 4
- -10^9 <= rec1[i], rec2[i] <= 10^9
- rec1 and rec2 represent a valid rectangle with a non-zero area.

## 해석 및 풀이 방식
이거 쉽게 아는 수식이있는데 기억이 안난다.

4개의 점 중 하나라도 사각형 안에 있으면 overlab 됨.

rec1 사각형 안에 rec2가 포함되는 경우

rec2 사각형 안에 rec1이 포함되는 경우

### 알고리즘
- 수학

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
