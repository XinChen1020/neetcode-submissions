from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Top down DP
        # at each point, choose to take or skip the coin
        # and see if it can reach the amount 
        # This is easier to translate to 2d bottom up dp
        
        @cache
        def dfs(curr_idx, curr_amount):
            if curr_amount == amount:
                return 1
            
            if curr_idx == len(coins):
                return 0
            
            result = 0
            
            # Skip
            result = dfs(curr_idx + 1, curr_amount)

            # Take
            if coins[curr_idx] + curr_amount <= amount:
                result += dfs(curr_idx, curr_amount + coins[curr_idx])
            
            return result
        
        return dfs(0, 0)