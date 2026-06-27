class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        comp = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            for nei in adj[node]:
                # No need for tracking the parent node since
                # we don't care if go backs
                dfs(nei)

            return
        
        
        for v in range(n):
            if v in visited:
                continue
            comp += 1
            dfs(v)
        
        return comp
