from bisect import bisect_right
from functools import lru_cache


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # (left, right, weight, original_index)
        arr = [
            (l, r, w, idx)
            for idx, (l, r, w) in enumerate(intervals)
        ]

        # 시작점 기준 정렬
        arr.sort(key=lambda x: x[0])

        n = len(arr)
        starts = [arr[i][0] for i in range(n)]

        # next_idx[i]:
        # i번 interval을 선택했을 때 다음으로 선택 가능한 첫 interval
        next_idx = [0] * n

        for i in range(n):
            _, r, _, _ = arr[i]

            # 경계를 공유해도 겹치는 것이므로
            # next interval의 left는 r보다 "커야" 함
            next_idx[i] = bisect_right(starts, r)

        def better(a, b):
            """
            a, b = (score, indices_tuple)

            1. score가 큰 쪽
            2. score가 같으면 lexicographically smaller한 쪽
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        @lru_cache(None)
        def dp(i, k):
            """
            i번째 interval부터 보면서
            최대 k개를 선택했을 때의 최적 결과.

            return:
                (score, sorted_indices_tuple)
            """
            if i >= n or k == 0:
                return (0, ())

            # 1. 현재 interval을 선택하지 않음
            skip = dp(i + 1, k)

            # 2. 현재 interval을 선택
            _, _, w, original_idx = arr[i]

            next_score, next_indices = dp(next_idx[i], k - 1)

            # lexicographical comparison을 위해
            # 원본 index 배열은 항상 정렬된 상태로 유지
            chosen_indices = tuple(
                sorted((original_idx,) + next_indices)
            )

            take = (
                w + next_score,
                chosen_indices
            )

            return better(skip, take)

        return list(dp(0, 4)[1])