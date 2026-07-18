from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # DFS with memorization

        @cache
        def dfs(i, j):

            # Formed t successfully
            # basically asking occurance of t[j:] = "" in s[i:]
            # which there's only 1 way -> ignore everything
            if j == len(t):
                return 1
            
            # Run out s, nothing forming
            # asking occurance of t[j:] in s[i:] = ""
            # which you can't
            if i == len(s):
                return 0

            if s[i] == t[j]:
                # if matched, two sub problem
                # 1) find occurance of the rest of t in the rest of s
                # 2) find occurance of whole t in the rest of s
                # sum them 
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If not matched:
                # Simply keep finding occurance of t in the rest of s
                return dfs(i + 1, j)

        return dfs(0, 0)