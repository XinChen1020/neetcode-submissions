class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        smallest = min(coins)
        if amount == 0:
            return 0
        if smallest > amount:
            return -1

        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(smallest, amount + 1):
            r = []
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1
