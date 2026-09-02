from bisect import bisect_left


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        prefix = [0]
        for value in stoneValue:
            prefix.append(prefix[-1] + value)

        dp = [[0] * n for _ in range(n)]

        # best_left[i][j]:
        # max(sum(i..k) + dp[i][k]) for i <= k <= j
        best_left = [[0] * n for _ in range(n)]

        # best_right[i][j]:
        # max(sum(k..j) + dp[k][j]) for i <= k <= j
        best_right = [[0] * n for _ in range(n)]

        for i, value in enumerate(stoneValue):
            best_left[i][i] = value
            best_right[i][i] = value

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # prefix[r] - prefix[i]가 왼쪽 구간 합.
                # r은 분할 위치이며 i+1 <= r <= j.
                balance = prefix[i] + prefix[j + 1]
                r = bisect_left(
                    prefix,
                    (balance + 1) // 2,
                    i + 1,
                    j + 1,
                )

                score = 0

                # 정확히 반으로 나뉘면 양쪽 모두 선택 가능
                if r <= j and balance % 2 == 0 and prefix[r] * 2 == balance:
                    score = max(
                        best_left[i][r - 1],
                        best_right[r][j],
                    )
                else:
                    # r보다 왼쪽 분할: 왼쪽이 더 작음
                    if r - 2 >= i:
                        score = max(score, best_left[i][r - 2])

                    # r부터의 분할: 오른쪽이 더 작음
                    if r <= j:
                        score = max(score, best_right[r][j])

                dp[i][j] = score

                total = prefix[j + 1] - prefix[i]
                best_left[i][j] = max(best_left[i][j - 1], total + dp[i][j])
                best_right[i][j] = max(best_right[i + 1][j], total + dp[i][j])

        return dp[0][n - 1]