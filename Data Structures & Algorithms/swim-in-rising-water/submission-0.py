from _heapq import heapify
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Diji ?
        # Swiming doesn't take time
        # Minimize the max in the route from (0, 0) to (n-1, n-1)

        directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        dist = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        dist[0][0] = grid[0][0]

        heap = [[grid[0][0], 0, 0]]


        n = len(grid)

        while heap:
            time, i, j = heapq.heappop(heap)

            if time > dist[i][j]:
                continue
            
            if i == n - 1 and j == n - 1:
                
                return dist[i][j]
            
            for di, dj in directions:
                new_i = di + i
                new_j = dj + j
                if not ( 0 <= new_i < n and 0 <= new_j < n):
                    continue

                if max(grid[new_i][new_j], dist[i][j]) < dist[new_i][new_j]:
                    dist[new_i][new_j] = max(grid[new_i][new_j], dist[i][j])
                    heapq.heappush(heap, [dist[new_i][new_j], new_i, new_j])
        return -1

        