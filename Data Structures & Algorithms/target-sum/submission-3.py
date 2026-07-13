from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(curr_idx, remainder):
            
            if curr_idx >= len(nums):
                return remainder == 0 
            
            # plus
            result = dfs(curr_idx + 1, remainder - nums[curr_idx])

            # negative
            result += dfs(curr_idx + 1, remainder + nums[curr_idx])

            return result


        return dfs(0, target)