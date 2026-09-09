class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijk but only keep

        # Graph construction
        weighted_adj = [[] for _ in range(n)]

        for u, v, w in flights:
            weighted_adj[u].append((v, w))
        heap = [[0, -1, src]]

        # Need extra states since the future option for 
        # arriving a node with 2 stop and 3 stops are different
        # we don't care if the stop if more than k
        distance = [[float("inf")] * (k + 2) for _ in range(n)]
        distance[src][0] = 0

        while heap:

            dist, stop, node = heapq.heappop(heap)

            if node == dst:
                return dist

            if stop == k or distance[node][stop + 1] < dist:
                continue
            
            for nei, w in weighted_adj[node]:

                if dist + w < distance[nei][stop + 2]:
                    distance[nei][stop + 2] = dist + w
                    heapq.heappush(heap, [dist + w, stop + 1, nei])

        return -1
        
        
