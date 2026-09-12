## [3414. Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/description/?envType=daily-question&envId=2026-09-12)

**난이도:** 🔴 Hard

### 문제 설명
You are given a 2D integer array intervals, where intervals[i] = [l_i, r_i, weight_i]. Interval i starts at position l_i and ends at r_i, and has a weight of weight_i. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

Example 1:
- Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
- Output: [2,3]
- Explanation:

    You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:
- Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
- Output: [1,3,5,6]
- Explanation:

    You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

Constraints:
- 1 <= intevals.length <= 5 * 10^4
- intervals[i].length == 3
- intervals[i] = [l_i, r_i, weight_i]
- 1 <= l_i <= r_i <= 10^9
- 1 <= weight_i <= 10^9

## 해석 및 풀이 방식
1. l을 기준으로 정렬
2. i를 선택했을 때 다음에 선택가능한 idx 계산 (21:28)
3. 현재 interval 을 선택하는 경우와 선택하지 않는 경우 중 더 나은 경우의 수 선택

### 알고리즘
- 정렬
- 이분탐색
- DP

### 시간복잡도: O(nlogn + 4n)

### 공간복잡도:

## 다른사람들의 개쩌는답
https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/solutions/8516767/interval-dp-one-min-for-the-tiebreak-on-uddbc/?envType=daily-question&envId=2026-09-12

접근은 비슷한데 코드가 더 간결 

겁나어렵네 ;;