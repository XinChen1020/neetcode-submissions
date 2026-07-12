class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom up DP
        # Go from right to left
        # dp[i][j] = max profit you get from each state i using prices[j:]
        # let states be holding (1), not holding (0)

        dp = [[0] * (len(prices) + 2) for _ in range(2)]

        for j in range(len(prices) - 1, -1 , -1):
            for holding in range(2):
                if holding:
                    # Keep
                    skip = dp[1][j + 1]

                    sell = prices[j] + dp[0][j + 2]

                    dp[1][j] = max(skip, sell)
                else:
                    # stay not holding
                    skip = dp[0][j + 1]

                    # buy today
                    buy = -prices[j] + dp[1][j + 1]

                    dp[0][j] = max(skip, buy)

        return dp[0][0]
