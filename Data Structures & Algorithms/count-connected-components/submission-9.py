class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def bfs(node):
            queue = deque([node])

            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nei in adj[node]:
                    queue.append(nei)
        comp = 0
        for v in range(n):
            if v not in visited:
                comp += 1
                bfs(v)
        
        return comp
