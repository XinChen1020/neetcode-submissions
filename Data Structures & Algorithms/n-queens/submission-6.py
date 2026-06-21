class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                results.append(board.copy())
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                row_str = "." * col + "Q" + "." * (n - col - 1)

                board.append(row_str)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return results