from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            if target ** 0.5 == int(target ** 0.5):
                dp[target] = 1

            for i in range(1, isqrt(target) + 1):
                dp[target] = min(
                    dp[target],
                    1 + dp[target - i * i]
                )

        return dp[n]