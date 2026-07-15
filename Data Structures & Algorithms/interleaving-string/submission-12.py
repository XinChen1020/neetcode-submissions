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
        s1_len = len(s1)
        s2_len = len(s2)
        
        if len(s1) + len(s2) != len(s3):
            return False

        # Tiny optimized so keep the array small
        if s2_len > s1_len:
            s1, s2 = s2, s1
            s1_len, s2_len = s2_len, s1_len
            
        dp = [False] * (s2_len + 1)
        dp[s2_len] = True

        for i in range(s1_len, -1 , -1):
            for j in range(s2_len, -1, -1):
                if i == s1_len and j == s2_len:
                    continue
                s1_condition = i < s1_len and dp[j] and s1[i] == s3[i + j]
                s2_condition = j < s2_len and dp[j + 1] and s2[j] == s3[i + j]

                dp[j] = s1_condition or s2_condition
                
        return dp[0]
            
