class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Find the tresure chest
        # Use BFS to assign each reachable land a value (min distance)
        search_directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        def bfs(i, j) -> None:
            visited = set((i, j))
            queue = deque([(i, j, 0)])

            while queue:
                i, j, distance = queue.popleft()
                for d in search_directions:
                    new_i = i + d[0]
                    new_j = j + d[1]

                    if 0 > new_i or new_i >= len(grid) or \
                    0 > new_j or new_j >= len(grid[0]) or \
                    grid[new_i][new_j] == -1 or (new_i, new_j) in visited:
                        continue
                    grid[new_i][new_j] = min(grid[new_i][new_j], distance + 1)
                    queue.append((new_i, new_j, distance + 1))
                    visited.add((new_i, new_j))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)
        

