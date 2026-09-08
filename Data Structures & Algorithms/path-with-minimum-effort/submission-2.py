class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Weighted graph -> each cell represent node, positive weight only
        # dijkstra doesn't need to have graph first!!!!

        r, c = len(heights), len(heights[0])

        # distance, i, j
        min_heap = [[0, 0, 0]]

        distances = [[float("inf")] * c for _ in range(r)]

        distances[0][0] = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        while min_heap:
            dis, i, j = heapq.heappop(min_heap)

            if dis > distances[i][j]:
                continue
                
            if (i, j) == (r - 1, c - 1):
                return dis

            for di, dj in directions:
                new_i = di + i
                new_j = dj + j
                if not (0 <= new_i < r and 0 <= new_j < c):
                    continue

                new_dis = max(abs(heights[new_i][new_j] - heights[i][j]), dis)
                if new_dis < distances[new_i][new_j]:
                    distances[new_i][new_j] = new_dis
                    heapq.heappush(min_heap, [new_dis, new_i, new_j])

        return distances[-1][-1]