class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*38
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for idx in range(3, n+1):
            dp[idx] = dp[idx-3] + dp[idx-2] + dp[idx-1]

        return dp[n]