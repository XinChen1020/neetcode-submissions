class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0
        for p in prices:
            min_p = min(p, min_p)
            max_profit = max(p - min_p, max_profit)
        
        return max_profit