class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = defaultdict(set)

        for w in wordDict:
            word_set[len(w)].add(w)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for r in range(1, len(dp)):
            for length, w_set in word_set.items():
                if r - length < 0:
                    continue
                
                if dp[r-length] and s[r-length:r] in w_set:
                    dp[r] = True
        return dp[-1]