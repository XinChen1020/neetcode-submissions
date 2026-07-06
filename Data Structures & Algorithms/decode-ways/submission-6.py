from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(j):
            # Empty prefix has one valid decoding
            if j == 0:
                return 1

            ways = 0

            # Use the last 1 digit
            if s[j - 1] != "0":
                ways += dfs(j - 1)

            # Use the last 2 digits
            if j - 2 >= 0 and 10 <= int(s[j - 2:j]) <= 26:
                ways += dfs(j - 2)

            return ways

        return dfs(len(s))