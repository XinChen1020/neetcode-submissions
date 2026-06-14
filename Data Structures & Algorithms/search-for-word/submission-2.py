class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        def dfs(i, j, correct_count, seen):
            if correct_count == len(word):
                return True

            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and board[new_i][new_j] == word[correct_count] and (new_i, new_j) not in seen:
                    seen.add((i, j))
                    if dfs(new_i, new_j, correct_count + 1, seen):
                        return True
                    seen.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, set()):
                        return True
        
        return False