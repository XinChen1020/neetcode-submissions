class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # Graph construction
        adj = [[] for _ in range(n)]
        
        for u, v, w in times:
            adj[u - 1].append([w, v - 1])

        heap = [[0, k - 1]]
        distances = [float("inf")] * n
        distances[k - 1] = 0
        while heap:
            t, u = heapq.heappop(heap)

            if t > distances[u]:
                continue
            
            for w, v in adj[u]:
                if t + w < distances[v]:
                    distances[v] = t + w
                    heapq.heappush(heap, [t + w, v])
        result = max(distances)
        if result == float("inf"):
            return -1
        else:
            return result