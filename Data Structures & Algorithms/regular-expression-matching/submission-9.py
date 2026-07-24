from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom up DP
        # dp[i][j] = able to match with s[i:] using p[j:]
        # Space optimized
        # Only need previous row
        dp = [False] * (len(p) + 1)

        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            prev = dp[-1]
            dp[-1] = i == len(s)

            for j in range(len(p) - 1, -1, -1):
                temp = dp[j]

                # we shouldn't do anything for p[j:] that starts with * since
                # that invalid
                if p[j] == "*":
                    dp[j] = False
                else:
                    matched = (i < len(s) and (s[i] == p[j] or p[j] == "."))

                    if j + 1 < len(p) and p[j + 1] == "*":
                        dp[j] = dp[j + 2] or (matched and dp[j])
                    
                    else:
                        dp[j] = prev and matched
                
                prev = temp


        return dp[0]
        

