class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        search_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            count = 1
            
            if 0 > i or len(grid) <= i or \
            0 > j or len(grid[0]) <= j or \
            grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            for d in search_dir:
                count += dfs(i + d[0], j + d[1])
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
                    
            
        return result