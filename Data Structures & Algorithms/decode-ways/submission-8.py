from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up dp
        # dp[i] = # of way decoding using s[:i]
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        for j in range(1, len(s) + 1):
            if s[j - 1] != "0":
                dp[j] += dp[j - 1]
            if j - 2 >= 0 and 10 <= int(s[j - 2:j]) <= 26:
                dp[j] += dp[j - 2]

        return dp[-1]