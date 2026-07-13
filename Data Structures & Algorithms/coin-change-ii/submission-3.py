from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom up DP (suffix version)
        # at each point, choose to take or skip the coin
        # and see if it can reach the amount
        # dp[i][j] = ways to reach amount j using coins[i:]

        dp = [[1] + [0] * amount for _ in range(len(coins) + 1)]

        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount + 1):

                # skip
                dp[i][j] = dp[i + 1][j]
                
                if j >= coins[i]:
                    # take -> use same i since we can reuse coin
                    dp[i][j] += dp[i][j - coins[i]]
                    
        return dp[0][amount]