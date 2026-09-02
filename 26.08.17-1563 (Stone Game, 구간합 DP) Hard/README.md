## [1563. Stone Game V](https://leetcode.com/problems/stone-game-v/description/?envType=daily-question&envId=2026-08-17)

### 문제 설명
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

Example 1:
- Input: stoneValue = [6,2,3,4,5,5]
- Output: 18
- Explanation: 
    - In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
    - In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
    - The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:
- Input: stoneValue = [7,7,7,7,7,7,7]
- Output: 28

Example 3:
- Input: stoneValue = [4]
- Output: 0

Constraints:
- 1 <= stoneValue.length <= 500
- 1 <= stoneValue[i] <= 10^6

## 해석 및 풀이 방식
나눌 때 정확히 반으로 나누지 않고 최대한 버리는 양과 가져갈 수 있는 양이 적게 처리되어야지 이득임

예를들어 [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 이라면 가운데서 자르는 것 보다 10에서 자르는게 더 높은 점수를 얻을 수 있음 -> 어느 부분에서 잘라야지 왼쪽 오른쪽이 가장 균형될까?

O(N) 으로 가장 효율적인 부분을 구할 수 있음

그리고 돌의 개수는 반씩 줄어드니 O(log N) 의 시간이 소요됨

---

단순히 이렇게 하면 될 줄 알았는데 만약 왼쪽 오른쪽 합이 같다면 최종적으로는 아래까지 확인해봐야함.

---

"두 부분의 합이 가장 비슷한 분할 하나”를 고르는 그리디는 반례가 있음 
- 반례: stoneValue = [2, 2, 2, 5]
- 그리디: [2,2,2] | [5] → 6 vs 5, 점수 5, 바로 종료 → 총 5
- 최적: [2,2] | [2,5] → 4 vs 7, 점수 4, 남은 [2,2]에서 다시 +2 → 총 6

따라서 분할을 고르는 그리디는 올바르지 못한답임.

[정답]

dp(i, j)를 i부터 j까지 돌이 남았을 때 얻을 수 있는 최대 점수라고 정의합니다.

돌 하나만 있으면 더 이상 점수를 얻을 수 없습니다.

```
dp(i, i) = 0
```

`k`에서 나눈다면:

```
left_sum  = sum(i ... k)
right_sum = sum(k+1 ... j)
```

점화식은 다음과 같습니다.

```
if left_sum < right_sum:
    candidate = left_sum + dp(i, k)
elif left_sum > right_sum:
    candidate = right_sum + dp(k + 1, j)
else:
    candidate = left_sum + max(dp(i, k), dp(k + 1, j))
```

그리고 가능한 모든 k 중 최댓값을 택합니다.

[가장 쉬운 버전]
`solution_normal_dp.py` 이 버전은 논리적으로 가장 이해하기 쉽습니다.

하지만 시간 복잡도는 O(n³)입니다.

구간 개수: O(n²)

각 구간에서 모든 분할점 탐색: O(n)

n = 500이면 Python에서는 다소 느릴 수 있습니다.

[최적화]

돌 값이 모두 양수라서, 왼쪽 구간의 합은 분할점을 오른쪽으로 옮길수록 계속 커집니다.

```
왼쪽 합 < 오른쪽 합
왼쪽 합 < 오른쪽 합
왼쪽 합 == 오른쪽 합  (있을 수도 있음)
왼쪽 합 > 오른쪽 합
왼쪽 합 > 오른쪽 합
```

여기서 중요한 점은:

“경계점 근처 하나만 선택”하는 것은 틀림

하지만 왼쪽이 작은 모든 분할 중 최댓값, 오른쪽이 작은 모든 분할 중 최댓값만 빠르게 찾으면 됨

아래 구현은 그 값을 누적 관리합니다. 시간 복잡도는 O(n² log n), 공간 복잡도는 O(n²)입니다.

`solution_optimal_dp.py` 확인

정리하면, 현재 접근은 “균형 분할이 좋은 후보가 될 수 있다”는 관찰 자체는 맞지만, 그 하나를 그리디하게 확정하는 부분이 틀렸습니다. 이 문제는 반드시 남은 구간의 미래 점수까지 포함한 구간 DP로 풀어야 합니다.

### 알고리즘

### 시간복잡도: 

### 공간복잡도: 

## 다른사람들의 개쩌는답
