class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up 2d dp
        # dp[i][j] = LCS length of text1[:i] and text2[:j]
        
        rows = len(text1)
        cols = len(text2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # If matched, we increase the length of LCS by 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If not matched, 
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[-1][-1]