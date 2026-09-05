from functools import cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        

        if s[-1] == "1":
            return False

        @cache
        def dfs(i):

            if i > len(s) - 1 or s[i] == "1":
                return False
            if i == len(s) - 1:
                return True
            
            for jump in range(min(maxJump, len(s) - i + 1), minJump - 1, -1):
                if dfs(i + jump):
                    return True

            return False
            
        
        return dfs(0)
            
                