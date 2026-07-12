from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(curr_idx, curr_amount):
            if curr_amount == amount:
                return 1
            result = 0
            for i in range(curr_idx, len(coins)):
                if curr_amount + coins[i] <= amount:
                    result += dfs(i, curr_amount + coins[i])
            return result
        
        return dfs(0, 0)