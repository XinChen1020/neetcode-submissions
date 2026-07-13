from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Top down DP
        # at each point, choose to take or skip the coin
        # and see if it can reach the amount 
        # This is easier to translate to 2d bottom up dp
        
        @cache
        def dfs(curr_idx, remainder):
            if remainder == 0:
                return 1
            
            if curr_idx == len(coins):
                return 0
            
            result = 0
            
            # Skip
            result = dfs(curr_idx + 1, remainder)

            # Take
            if remainder - coins[curr_idx] >= 0:
                result += dfs(curr_idx, remainder - coins[curr_idx])
            
            return result
        
        return dfs(0, amount)