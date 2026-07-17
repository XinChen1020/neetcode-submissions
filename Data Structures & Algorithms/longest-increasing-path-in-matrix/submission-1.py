from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS and record longest result
        
        row, col = len(matrix), len(matrix[0])
        result = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        @cache
        def dfs(i, j):
            result = 1

            for d_i, d_j in directions:
                new_i = i + d_i
                new_j = j + d_j

                if 0 <= new_i < row and 0 <= new_j < col \
                and matrix[i][j] < matrix[new_i][new_j]:
                    result = max(result, 1 + dfs(new_i, new_j))
            
            return result 

        for i in range(row):
            for j in range(col):
                result = max(result, dfs(i, j))
        
        return result