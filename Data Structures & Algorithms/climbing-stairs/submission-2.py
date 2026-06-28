class Solution:
    def climbStairs(self, n: int) -> int:
        # forward DP
        # dp[i] = # of ways to reach step i
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n + 1):
            if i + 1 <= n:
                dp[i + 1] += dp[i]
            if i + 2 <= n:
                dp[i + 2] += dp[i]

        return dp[-1]