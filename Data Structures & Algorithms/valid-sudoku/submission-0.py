class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_visited = set()
        col_visited = set()
        box_visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if (i, board[i][j]) not in row_visited:
                        row_visited.add((i, board[i][j]))
                    else:
                        return False
                    
                    if (j, board[i][j]) not in col_visited:
                        col_visited.add((j, board[i][j]))
                    else:
                        return False
                    
                    if (i//3, j//3,  board[i][j]) not in box_visited:
                        box_visited.add((i//3, j//3, board[i][j]))
                    else:
                        return False
        
        return True