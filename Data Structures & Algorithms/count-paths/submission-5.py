class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom-up dp -> space optimized since only depends on previous row
        # dp[i][j] = # of possible unique path to reach grid[i][j]

        dp = [1] * n

        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]