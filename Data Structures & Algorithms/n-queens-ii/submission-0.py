class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        col = set()
        diag1 = set()
        diag2 = set()

        def dfs(r):
            nonlocal result
            if r == n:
                result += 1
                return

            for c in range(n):
                if c in col or r + c in diag1 or r - c in diag2:
                    continue
                col.add(c)
                diag1.add(r + c)
                diag2.add(r - c)

                dfs(r + 1)

                col.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)
                
        
        dfs(0)

        return result