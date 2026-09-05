class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, count):

            if i >= len(board) or i < 0 or \
            j >= len(board[0]) or j < 0 or \
            board[i][j] != word[count]:
                return False

            if count == len(word) - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = "#"
            for d in directions:
                new_i = d[0] + i
                new_j = d[1] + j

                if dfs(new_i, new_j, count + 1):
                    return True

            board[i][j] = temp

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False