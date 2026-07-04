class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [False] * len(s)
        result = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                dp[j] = s[i] == s[j] and (j - i <= 2 or dp[j - 1])

                if dp[j]:
                    result += 1

        return result