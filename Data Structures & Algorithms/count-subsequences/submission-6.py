from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Bottom up DP
        # dp[i][j] = distinct subsequence of s[i:] that are equals t[j:]
        # need to add 1 based on this def
        # Space optimized version
        # only need previous row
        dp = [0] * (len(t) + 1)

        # base condition
        dp[-1] = 1

        for i in range(len(s) - 1, -1 , -1):
            prev = dp[-1]
            for j in range(len(t) - 1, -1, -1):
                temp = dp[j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = temp
        
        return dp[0]