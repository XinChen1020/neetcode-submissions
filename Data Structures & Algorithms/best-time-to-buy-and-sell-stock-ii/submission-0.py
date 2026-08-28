class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can buy and sell on the same day
        # any number of transactions
        # at most 1 share of stock at any time
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]

        
        return result