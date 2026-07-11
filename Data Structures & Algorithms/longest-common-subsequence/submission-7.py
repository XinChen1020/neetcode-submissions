class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Space optimzed bottom up 2d dp
        # dp[i][j] = LCS length of text1[:i] and text2[:j]
        
        rows = len(text1)
        cols = len(text2)

        dp = [0] * (cols + 1)

        for i in range(1, rows + 1):
            prev = dp[0]
            for j in range(1, cols + 1):
                temp = dp[j]
                # If matched, we increase the length of LCS by 1
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    # If not matched, you get the max result that you could get
                    # by ignorning text1[i] or text2[j]
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        
        return dp[-1]