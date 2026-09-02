from functools import cache


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        prefix = [0]
        for value in stoneValue:
            prefix.append(prefix[-1] + value)

        def get_sum(left: int, right: int) -> int:
            return prefix[right + 1] - prefix[left]

        @cache
        def dp(left: int, right: int) -> int:
            if left == right:
                return 0

            answer = 0

            for mid in range(left, right):
                left_sum = get_sum(left, mid)
                right_sum = get_sum(mid + 1, right)

                if left_sum < right_sum:
                    answer = max(answer, left_sum + dp(left, mid))

                elif left_sum > right_sum:
                    answer = max(answer, right_sum + dp(mid + 1, right))

                else:
                    answer = max(
                        answer,
                        left_sum + dp(left, mid),
                        right_sum + dp(mid + 1, right),
                    )

            return answer

        return dp(0, n - 1)