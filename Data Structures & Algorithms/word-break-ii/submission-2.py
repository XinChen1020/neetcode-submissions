from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        results = []
        wordDict = set(wordDict)
        min_len = min(len(w) for w in wordDict)
        max_len = max(len(w) for w in wordDict)

        @cache
        def dfs(i, curr_comb):

            if i == len(s):
                results.append(curr_comb)
                return

            for j in range(i + min_len, i + max_len + 1):
                if j > len(s):
                    break
                if s[i:j] not in wordDict:
                    continue
                if curr_comb:
                    dfs(j, " ".join([curr_comb, s[i:j]]))
                else:
                    dfs(j, s[i:j])


        dfs(0, "")
        return results

