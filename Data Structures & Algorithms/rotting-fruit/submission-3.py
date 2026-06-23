class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start bfs from each rotten fruit.
        # minimum number of min is the max distance between
        # rotten fruit and fresh fruit when all rotten fruit start
        # bfs at the same time
        result = 0
        queue = deque([])
        search_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        

        def bfs():
            nonlocal result
            while queue:
                i, j, minute = queue.popleft()
                result = max(result, minute)
                for d in search_dir:
                    new_i = i + d[0]
                    new_j = j + d[1]

                    if 0 > new_i or new_i >= len(grid) or \
                    0 > new_j or new_j >= len(grid[0]) or \
                    grid[new_i][new_j] != 1:
                        continue

                    # Mark rotten before visiting so the same fresh
                    # orange wouldn't get add twice by two nearby rotten
                    # organe
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j, minute + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        bfs()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return result
