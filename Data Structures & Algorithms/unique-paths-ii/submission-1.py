class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    top = obstacleGrid[i - 1][j] if i > 0 else 0
                    left = obstacleGrid[i][j - 1] if j > 0 else 0

                    obstacleGrid[i][j] = top + left

        return obstacleGrid[-1][-1]