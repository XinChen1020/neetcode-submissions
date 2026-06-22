class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Add all tresure chest to the queue
        # Use BFS to assign each reachable land a value (min distance)
        # Since all tresure chest are processed one after another
        # whatever reached the land first, min distance would get assigned
        # O(m * n)
        search_directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        queue = deque([])
        visited = set()

        def bfs() -> None:

            while queue:
                i, j, distance = queue.popleft()
                for d in search_directions:
                    new_i = i + d[0]
                    new_j = j + d[1]

                    if 0 > new_i or new_i >= len(grid) or \
                    0 > new_j or new_j >= len(grid[0]) or \
                    grid[new_i][new_j] == -1 or (new_i, new_j) in visited:
                        continue
                    grid[new_i][new_j] = distance + 1
                    queue.append((new_i, new_j, distance + 1))
                    visited.add((new_i, new_j))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i,j))
        bfs()
        

