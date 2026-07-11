from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # For each price,
        # either sell, buy, or keep
        # can't buy when holding the coin or sold yesterday
        # 
        @cache
        def dfs(i, holding):
            if i >= len(prices):
                return 0

            # if not holding a coin
            if not holding:
                # Buy or Skip
                return max(-prices[i] + dfs(i + 1, True), dfs(i + 1, holding))

            else:
                # Note:
                # If sold, you can't do anything the next day
                # can't buy due to cool down, can't sell since have no coin
                # Skip to the day after
                
                # Sell or Skip
                return max(prices[i] + dfs(i + 2, False), dfs(i + 1, holding))
        
        return dfs(0, False)