from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom up DP
        # dp[i][j] = min opertion for word1[i:] to word2[j:]
        # Space optimized
        
        m, n = len(word1), len(word2)

        # Use shorter word to further optimized
        if n > m:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)

        # Base conditions
        for j in range(n + 1):
            dp[j] = n - j
        
        
        for i in range(m - 1, -1, -1):

            # Take care of the dignoal one
            prev = dp[-1]

            # Base condition
            dp[-1] = m - i
            
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], 
                    prev, 
                    dp[j + 1]) + 1
                prev = temp
        
        return dp[0]
