class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                top = grid[i][j - 1] if j - 1 >= 0 else float("inf")
                left = grid[i - 1][j] if i - 1 >= 0 else float("inf")
                grid[i][j] =  grid[i][j] + min(top, left)

        return grid[-1][-1]