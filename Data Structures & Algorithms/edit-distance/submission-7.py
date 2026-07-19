from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DFS with memorization
        
        m, n = len(word1), len(word2)
        
        @cache
        def dfs(i, j):

            if i == m:
                return n - j
            if j == n:
                return m - i

            if word1[i] == word2[j]:
                # If matched, solve the sub problem of min operation in the rest of the string
                return dfs(i + 1, j + 1)
            else:
                # If not matched, three possiblilities and each plus one operation
                return min(dfs(i + 1, j) + 1, # delete
                dfs(i + 1, j + 1) + 1, # replace
                dfs(i, j + 1) + 1 # insert
                )
        
        return dfs(0, 0)