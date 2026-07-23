class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bruto force -> DFS
        # i -> index of s, j -> index of p
        # if exact matched or ., i + 1, j + 1
        # if fuzzy match,
        #     * -> multiple possibility

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
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