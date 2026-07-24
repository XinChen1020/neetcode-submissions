from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom up DP
        # dp[i][j] = able to match with s[i:] using p[j:]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):

                # we shouldn't do anything for p[j:] that starts with * since
                # that invalid
                if p[j] == "*":
                    continue
                
                matched = (i < len(s) and (s[i] == p[j] or p[j] == "."))

                if j + 1 < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (matched and dp[i + 1][j])

                    # Important: so don't overwrite the result
                    continue
                
                if matched:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]
        

