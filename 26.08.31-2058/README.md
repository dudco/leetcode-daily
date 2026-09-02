## [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2026-08-31)

### 문제 설명
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:
- Input: head = [3,1]
- Output: [-1,-1]
- Explanation: There are no critical points in [3,1].

Example 2:
- Input: head = [5,3,1,2,5,1,2]
- Output: [1,3]
- Explanation: There are three critical points:
    - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
    - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
    - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
    
    The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
    
    The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:
- Input: head = [1,3,2,2,3,2,2,2,7]
- Output: [3,3]
- Explanation: There are two critical points:
    - [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
    - [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
    
    Both the minimum and maximum distances are between the second and the fifth node.
    
    Thus, minDistance and maxDistance is 5 - 2 = 3.
    
    Note that the last node is not considered a local maxima because it does not have a next node.
 

Constraints:
- The number of nodes in the list is in the range [2, 10^5].
- 1 <= Node.val <= 10^5
## 해석 및 풀이 방식
1. 크리티컬 포인트의 위치를 찾기
2. 해당 위치에서의 크리티컬포인트를 찾으면 이전 크리티컬 포인트와 비교하여 min, max 거리 계산
3. min, max 거리 계산은 어떻게 할 수 있을까?
    1. 첫번째로 찾은 크리티컬 포인트는 위치만 저장
    2. 두번째부터 찾은 크리티컬 포인트를 기준으로 min, max 위치 업데이트.
    3. 세번째 크리티컬 포인트부터는 첫번째와 비교하면 무조건 먼 위치이므로 max 업데이트는 필수
    4. 세번째 크리티컬 포인트와 두번째를 마지막 크리티컬 포인트를 비교, 가장 작은 크리티컬 포인트일수도
### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/solutions/8492257/solution-by-la_castille-87j1/?envType=daily-question&envId=2026-08-31

min, max 구해놓고 max는 내가한것처럼 항상 새로운거 찾으면 업데이트해주면되는 방식, min은 그 때 그 때 검사하는 방식을 이용함.

비슷한데 코드가 좀 더 짧고 간결해서 좋아보임

[[Min, c[0] - c[1]], [-1, -1]][not c[1]] -> 이런 문법은 신박 근데 chatgpt 피셜 일반 삼항연산자가 더 좋다고하긴함. 연산을 안해서