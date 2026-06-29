class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result_idx, result_len = 0, 0
        # dp[i]][j] -> whether the s[i:j + 1] is palindrome or not
        dp = [[False] * len(s) for _ in range(len(s))]
        
        for i in range(len(s) -1 , -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j + 1 - i > result_len:
                        result_len = j - i + 1
                        result_idx = i
        return s[result_idx: result_idx + result_len]