from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        # bottom up DP solution
        # dp[i] = min step to reach nums[i]
        # O(n^2)
        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for dis in range(min(nums[i], len(nums) - 1 - i), 0, -1):
                dp[i] = min(1 + dp[i + dis], dp[i])
        return dp[0]
        
        
