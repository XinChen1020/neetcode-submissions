from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return True

            for j in range(min(nums[i], len(nums) - 1 - i), 0, -1):
                if dfs(i + j):
                    return True
        
            return False
        
        return dfs(0)