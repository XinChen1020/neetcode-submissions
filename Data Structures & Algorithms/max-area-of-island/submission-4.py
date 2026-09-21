class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        result = 0
        def dfs(i, j):
            
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == 0:
                return 0
            
            total = 1
            grid[i][j] = 0
            for di, dj in directions:
                new_i = di + i
                new_j = dj + j

                total += dfs(new_i, new_j)
            
            return total
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        return result