class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        comp = 0
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            for nei in adj[node]:
                # Prevent going back
                if nei == parent:
                    continue
                dfs(nei, node)

            return
        
        
        for v in range(n):
            if v in visited:
                continue
            comp += 1
            dfs(v, -1)
        
        return comp
