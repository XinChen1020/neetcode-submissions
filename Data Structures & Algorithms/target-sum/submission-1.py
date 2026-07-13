from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(curr_idx, curr_sum):
            
            if curr_idx >= len(nums):
                return curr_sum == target
            
            # plus
            result = dfs(curr_idx + 1, curr_sum + nums[curr_idx])

            # negative
            result += dfs(curr_idx + 1, curr_sum - nums[curr_idx])

            return result


        return dfs(0, 0)