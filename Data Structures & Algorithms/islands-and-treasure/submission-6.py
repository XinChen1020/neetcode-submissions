class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source BFS start from the chest

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])
        
        while queue:
            
            for _ in range(len(queue)):
                i, j, step = queue.popleft()

                for di, dj in directions:
                    new_i = di + i
                    new_j = dj + j

                    if not (0 <= new_i < m and 0 <= new_j < n) \
                    or grid[new_i][new_j] == -1 \
                    or grid[new_i][new_j] != 2147483647:
                        continue
                    grid[new_i][new_j] = step + 1
                    queue.append([new_i, new_j, step + 1])
                    
                    



