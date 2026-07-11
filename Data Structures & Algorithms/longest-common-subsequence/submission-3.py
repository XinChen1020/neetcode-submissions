from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down 2d dp
        # dfs(i, j) = LCS for text1[:i] and text2[:j]

        @cache
        def dfs(i, j):

            if i == 0 or j == 0:
                return 0
                
            if text1[i - 1] == text2[j - 1]:
                return dfs(i - 1, j - 1) + 1
            else:
                return max(dfs(i - 1, j), dfs(i, j - 1))

    
        return dfs(len(text1), len(text2))