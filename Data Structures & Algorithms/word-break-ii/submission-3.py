from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        min_len = min(len(w) for w in wordDict)
        max_len = max(len(w) for w in wordDict)

        @cache
        def dfs(i):

            if i == len(s):
                
                return [""]
            result = []

            for j in range(i + min_len, min(len(s), i + max_len) + 1):

                if s[i:j] not in wordDict:
                    continue
                for suffix in dfs(j):
                    if suffix:
                        result.append(s[i:j] + " " + suffix)
                    else:
                        result.append(s[i:j])

            return result


        return dfs(0)

