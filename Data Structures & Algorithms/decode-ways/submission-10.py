from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            result = dfs(i + 1)
            if i < len(s) - 1 and int(s[i:i + 2]) <= 26:

                result += dfs(i + 2)
            
            return result

        return dfs(0)