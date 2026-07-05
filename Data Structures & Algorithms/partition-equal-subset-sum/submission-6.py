from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DFS to try to find a subset such that it equals half of sum(nums)
        total = sum(nums)
        # odd total can't be split into subset with integer only
        if total % 2 != 0:
            return False
        
        @cache
        def dfs(curr_idx, target):
            if curr_idx  >= len(nums):
                return target == 0

            if target < 0:
                return False
            
            # Not Take or take
            return dfs(curr_idx + 1, target) or dfs(curr_idx + 1, target - nums[curr_idx])
        
        return dfs(0, total // 2)