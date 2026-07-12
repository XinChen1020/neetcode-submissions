class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom up DP with space optimization
        # Go from right to left
        # dp[i][j] = max profit you get from each state i using prices[j:]
        # let states be holding (1), not holding (0)
        # optimization: we only need dp[0][j + 1], dp[1][j + 1], dp[0][j + 2]


        dp_0_1, dp_0_2, dp_1_1 = 0, 0, 0
        

        for j in range(len(prices) - 1, -1 , -1):
            # Not holding
            new_dp_0_1 = max(dp_0_1, -prices[j] + dp_1_1)

            # Holding
            new_dp_1_1 = max(dp_1_1, prices[j] + dp_0_2)

            # Move backward
            dp_0_2 = dp_0_1

            dp_0_1 = new_dp_0_1
            dp_1_1 = new_dp_1_1

        return new_dp_0_1
