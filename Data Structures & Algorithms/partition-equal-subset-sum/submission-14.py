from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)

        if target % 2 != 0:
            return False
        
        target = target // 2

        # Can we pick a subset of nums such that
        # sum(subset) == target

        @cache
        def dfs(i, remaining):

            if i == len(nums):

                return remaining == 0
            
            # Skip or keep
            return dfs(i + 1, remaining) or dfs(i + 1, remaining - nums[i])
        
        return dfs(0, target)

