class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # khan algo
        # Since there n-1 edges, there's n node
        degree = [0] * (len(edges) + 1)
        adj = [[] for _ in range(len(edges) + 1)]
        
        # Craft adj list
        for u, v in edges:
            adj[u].append(v)
            degree[u] += 1
            adj[v].append(u)
            degree[v] += 1
        
        queue = deque([])
        for i in range(1, len(edges) + 1):
            if degree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            degree[node] -= 1

            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    queue.append(nei)
        
        for u, v in reversed(edges):
            if degree[u] > 0 and degree[v] > 0:
                return [u, v]
        return []


            


