from functools import cache
class Solution:
    def integerBreak(self, n: int) -> int:
        
        # Return max product for target
        @cache
        def dfs(target):
            if target == 1:
                return 1
            
            result = 0 if target == n else target
            for i in range(1, target // 2 + 1):
                result = max(result, dfs(i) * dfs(target - i))
            
            return result
        
        return dfs(n)