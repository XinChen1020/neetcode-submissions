class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        # Shortest path

        # Build adj and distance
        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v, t))
        dist = [float("inf")] * (n + 1)

        # Dijkstra
        dist[k] = 0
        heap = [(0, k)]
        visited = set()
        result = 0
        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            result = distance
            for nei, weight in adj[node]:
                if dist[nei] > dist[node] + weight:
                    dist[nei] = dist[node] + weight
                
                    heapq.heappush(heap, (dist[nei], nei))
        return result if len(visited) == n else -1

        