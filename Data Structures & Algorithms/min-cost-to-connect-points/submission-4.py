class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # min_dist[i] = cheapest cost currently known
        # to connect node i to the MST
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        cost = 0

        for _ in range(n):
            # Pick unvisited node with smallest connection cost
            node = -1
            for i in range(n):
                if not visited[i] and (
                    node == -1 or min_dist[i] < min_dist[node]
                ):
                    node = i

            # Add it to MST
            visited[node] = True
            cost += min_dist[node]

            x1, y1 = points[node]

            # Update cheapest connection for remaining nodes
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[i] = min(min_dist[i], dist)

        return cost