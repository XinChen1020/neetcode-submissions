from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Bottom UP dp
        # Match one character at a time
        # Decision points:
        # if s3[k] match only s1[i] or s2[j], only one path
        # if s3[k] match neither, return False for current path
        # if both matches, two path
        # dp[i][j] = whether we can create s3[i + j:] using s1[i:] and s2[j:]
        # Space optimized: only depends on previous/i + 1 row and j - 1
        
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True

        for i in range(len(s1), -1 , -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue
                s1_condition = i < len(s1) and dp[j] and s1[i] == s3[i + j]
                s2_condition = j < len(s2) and dp[j + 1] and s2[j] == s3[i + j]

                dp[j] = s1_condition or s2_condition
                
        return dp[0]
            
