class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking with DP
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
        
        print(dp)
        result = []
        stack = deque([[0, []]])

        while stack:
            # l = start of the next partition
            l, partitions = stack.pop()

            
            if l >= len(s):
                result.append(partitions)

            # Find the next potential partitions and add
            # to the list
            # r = end of the next partition/substring
            for r in range(l, len(s)):
                # Prune out partition if it's not forming a pailndrome
                if dp[l][r]:
                    next_partitions = partitions.copy()
                    next_partitions.append(s[l:r + 1])
                    stack.append([r + 1, next_partitions])

        return result