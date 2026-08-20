from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # DFS
        # use current number or not
        #
        @cache
        def dfs(remaining):

            if remaining == 0:
                return 1
            if remaining < 0:
                
                return 0
            result = 0
            
            for n in nums:
                result += dfs(remaining - n)
            
            return result
        
        return dfs(target)