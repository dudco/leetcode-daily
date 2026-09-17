## [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/?envType=daily-question&envId=2026-09-17)

**난이도:** 🟡 Medium

### 문제 설명
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:
- Input: arr = [3,2,2,4,3], target = 3
- Output: 2
- Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:
- Input: arr = [7,3,4,7], target = 7
- Output: 2
- Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:
- Input: arr = [4,3,2,6,2,3,4], target = 6
- Output: -1
- Explanation: We have only one sub-array of sum = 6.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 1000
- 1 <= target <= 10^8

## 해석 및 풀이 방식
더해서 target 이 되는 subarray 를 구하고 거기서 가장 작은 array 두개의 길이 합을 구하는 문제.

Tow Pointer 방식으로 0부터 시작해서 숫자를 더하기 시작. 

만약 누적값이 target과 같음 -> l, r 저장 (또는 r - l 저장 -> 몇개로 이뤄져있는지)

만약 누적값이 target보다 작음 -> r += 1

만약 누적값이 target보다 큼 -> l += 1

저장된 숫자들 중 가장 작은 두개를 합함

맨앞부터 진행해서 만들어진 subarray 가 최소 크기의 subarray가 아닐 수도 있음 

ex) arr=[2,1,3,3,2,3,1],target=6 에서는 [3,3], [2,1,3] 이 선택되어 답이 5가될 수 있음

만들 수 있는 가장 작은 배열이 최선이 아닐 수 있음

ex) arr=[1,1,1,2,2,2,4,4], target=6 에서는 [1,1,2,2] 대신 [2,2,2]를 선택함으로써 만들 수 있는 sub-array가 사라지면서 만들 수 없게됨

i구간까지 왔을 때 타겟이 만들어지는 가장 작은 subarray의 길이를 저장

만약 타겟을 만들어졌다면 현재 구간의 왼쪽과 겹치지 않는 이전구간 확인하여 최소값을 찾아낼 수 있음

### 알고리즘
- Two Pointer
- Array

### 시간복잡도: O(N*N)

### 공간복잡도: O(N)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/editorial/?envType=daily-question&envId=2026-09-17

Prefix Sum으로 target 구간 찾기

prefix_sum은 arr[0]부터 현재 위치 i까지의 누적합입니다.

어떤 구간 `arr[start + 1 : i + 1]`의 합은: `prefix_sum[i] - prefix_sum[start]`

이 값이 `target` 이어야 하므로: `prefix_sum[start] == prefix_sum[i] - target`

즉 현재 누적합이 prefix_sum일 때, 이전에 prefix_sum - target이 있었으면 그 사이 구간의 합은 target입니다.
```
if prefix_sum - target in seen:
    start = seen[prefix_sum - target]
    length = i - start
```

seen은 {누적합: 그 누적합이 등장한 인덱스} 형태입니다.

초기값인:

seen = {0: -1}


은 배열 맨 처음부터의 구간도 처리하기 위해 필요합니다. 예를 들어 arr[0] == target이면 현재 누적합이 곧 target이고, target - target == 0을 찾게 됩니다.

---

best[i]의 의미
best[i] 는 0 ~ i 범위에서 찾을 수 있는, 합이 target인 부분 배열의 최소 길이입니다.

매 반복마다 이전 최솟값을 그대로 가져옵니다.

`best[i] = best[i - 1] if i > 0 else INF`

그리고 현재 i에서 끝나는 target 구간을 찾았다면 더 짧은 값으로 갱신합니다.

best[i] = min(best[i], length)

---

겹치지 않는 두 구간 처리

현재 찾은 구간은: [start + 1 ... i]

이 구간과 겹치지 않으려면, 첫 번째 구간은 반드시 start 이하에서 끝나야 합니다.

그래서 best[start]를 더합니다.

`if start >= 0: answer = min(answer, length + best[start])`

length: 현재 구간의 길이

best[start]: 현재 구간보다 왼쪽에서 끝나는 가장 짧은 target 구간 길이

이렇게 하면 두 구간은 반드시 겹치지 않습니다.

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = float("inf")
        best = [INF] * len(arr)
        seen = {0: -1}

        prefix_sum = 0
        answer = INF

        for i, num in enumerate(arr):
            prefix_sum += num
            best[i] = best[i - 1] if i > 0 else INF

            if prefix_sum - target in seen:
                start = seen[prefix_sum - target]
                length = i - start

                if start >= 0:
                    answer = min(answer, length + best[start])

                best[i] = min(best[i], length)

            seen[prefix_sum] = i

        return -1 if answer == INF else answer
```