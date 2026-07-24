from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Bottom up DP
        # dp[i] = Able to reach the end from nums[i]
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 1, -1 , -1):
            for dis in range(min(nums[i], len(nums) - 1 - i), 0, -1):
                if dp[i + dis]:
                    dp[i] = True
        return dp[0]