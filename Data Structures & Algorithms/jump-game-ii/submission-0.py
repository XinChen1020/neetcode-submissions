from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Top bottom DP solution
        
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            min_dis = float("inf")
            for dis in range(min(nums[i], len(nums) - 1 - i), 0, -1):
                min_dis = min(min_dis, 1 + dfs(i + dis))
            
            return min_dis 
        
        return dfs(0)