class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            nonlocal grid
            # Don't need to return anything
            grid[i][j] = "0"

            for di, dj in directions:
                if 0 <= i + di < n and 0 <= j + dj < m and grid[i + di][j + dj] == "1":
                    dfs(i + di, j + dj)
            
        
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    
                    result += 1
                    dfs(i, j)

        return result