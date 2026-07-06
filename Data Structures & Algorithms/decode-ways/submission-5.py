from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            # We successfully decoded the whole string
            if i == len(s):
                return 1

            # A code cannot start with 0
            if s[i] == "0":
                return 0

            ways = 0

            # Take one digit
            ways += dfs(i + 1)

            # Take two digits if valid
            if i + 2 <= len(s) and int(s[i:i + 2]) <= 26:
                ways += dfs(i + 2)

            return ways

        return dfs(0)