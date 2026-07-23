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
            if i == len(s) and j == len(p):
                return True

            # They aren't equal but j reached the end first, this mean
            # not match
            # We don't check the other way around (i reached the end but j still have things left)
            # becuase we could potentially skip whatever left in j due to * pattern
            if j == len(p) and i != len(s):
                return False

            # Handle the * case first
            if j + 1 < len(p) and p[j + 1] == "*":

                # zero match
                if dfs(i, j + 2):
                    return True

                # one or more matches
                curr_i = i
                while (
                    curr_i < len(s)
                    and (s[curr_i] == p[j] or p[j] == ".")
                ):
                    curr_i += 1

                    if dfs(curr_i, j + 2):
                        return True

                return False

            # Normal character match
            if (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            ):
                if dfs(i + 1, j + 1):
                    return True

            return False

        return dfs(0, 0)