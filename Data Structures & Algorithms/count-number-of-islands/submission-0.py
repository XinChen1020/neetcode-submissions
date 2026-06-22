class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        search_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j, grid):

            grid[i][j] = "#"

            for d in search_direction:
                new_i = i + d[0]
                new_j = j + d[1]

                if 0 <= new_i < len(grid) and \
                0 <= new_j < len(grid[0]) and \
                grid[new_i][new_j] == "1":
                    dfs(new_i, new_j, grid)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j, grid)
                    

        return result