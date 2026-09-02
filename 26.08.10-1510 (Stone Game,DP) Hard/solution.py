class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            num = 1

            while num * num <= stones:
                square = num * num
                if not dp[stones - square]:
                    dp[stones] = True
                    break

                num += 1

        return dp[n]