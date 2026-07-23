from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bruto force -> DFS
        # i -> index of s, j -> index of p
        # if exact matched or ., i + 1, j + 1
        # if fuzzy match,
        #     * -> multiple possibility

        @cache
        def dfs(i, j):
            
            if j == len(p):
                return i == len(s)

            matched = (i < len(s) # This is to prevent crashing
                and (s[i] == p[j] or p[j] == "."))

            # Handle the * case first
            if j + 1 < len(p) and p[j + 1] == "*":

                # zero match
                return (dfs(i, j + 2) or (matched and dfs(i + 1, j)))


            # Normal character match
            if matched:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)