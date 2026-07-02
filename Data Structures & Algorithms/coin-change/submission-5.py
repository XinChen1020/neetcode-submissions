from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down DP
        
        @cache
        def dfs(amount):
            if amount == 0:
                return 0
                
            result = float("inf")
            for c in coins:
                if amount - c >= 0:
                    result = min(result, dfs(amount - c) + 1)
                
            return result
        result = dfs(amount)
        return result if result != float("inf") else -1