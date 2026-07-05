from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DFS
        total = sum(nums)
        # odd total can't be split into subset with integer only
        if total % 2 != 0:
            return False
        
        @cache
        def dfs(curr_idx, curr_sum):

            if curr_sum == total / 2:
                return True
            if curr_idx == len(nums) - 1:
                return False
            
            # Take
            if curr_sum + nums[curr_idx + 1] <= total / 2:
                if dfs(curr_idx + 1, curr_sum + nums[curr_idx + 1]):
                    return True

            # Not Take
            if dfs(curr_idx + 1, curr_sum):
                return True
            
            return False
        
        return dfs(-1, 0)