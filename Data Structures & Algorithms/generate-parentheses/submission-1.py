class Solution:
    def generateParenthesis(self, n):
        # DP
        # res[k] -> all valid parenthesis combin with k pairs
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            # Go through all previous valid combin that can be used
            # to fill left and right part (k-1 of them)
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)

        return res[-1]