class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prime algo
        # Use priority heap
        # Assume all point separate, start with a random point
        # always pick the minimal edge connect to Vs that
        # are currently in the MST to an outside Vs, which avoids cycle

        # distance from unvisited to visited node, idx
        heap = [[0, 0]]
        visited = [False] * len(points)
        cost = 0

        distance = lambda u, v: abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
        while heap:
            dist, node = heapq.heappop(heap)

            if visited[node]:
                continue

            cost += dist
            visited[node] = True

            for i in range(len(points)):
                if not visited[i]:
                    heapq.heappush(heap, [distance(node, i), i])
        return cost
        

