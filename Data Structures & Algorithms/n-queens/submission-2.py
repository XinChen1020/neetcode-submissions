import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        stack = deque([[0, [], [set(), set(), set()]]])
        # [current row, board, occupied]
        #[col, right to left diagonal (x + y), left to right diagonal (x - y)]
        while stack:
            i, board, occupied = stack.pop()

            if i == n:
                results.append(board)
                continue

            for j in range(n):
                if j not in occupied[0] and i - j not in occupied[1] and i + j not in occupied[2]:
                    new_board = copy.deepcopy(board)
                    new_occupied = copy.deepcopy(occupied)
                    new_board.append("".join(["." if b != j else "Q" for b in range(n)]))
                    new_occupied[0].add(j)
                    new_occupied[1].add(i - j)
                    new_occupied[2].add(i + j)

                    stack.append([i + 1, new_board, new_occupied]) 

        
        return results