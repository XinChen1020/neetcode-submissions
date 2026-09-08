class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # DFS?

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # cycle prevention
        visited = set()
        def dfs(u):
            if len(adj[u]) == 1 and adj[u][0] in visited:
                return 0
            
            max_height = 0
            visited.add(u)
            for v in adj[u]:
                if v in visited:
                    continue
                max_height = max(max_height, 1 + dfs(v))
            
            visited.remove(u)
            return max_height


        result = {}
        for i in range(n):
            result[i] = dfs(i)
        
        min_val = min(result.values())

        min_keys = [k for k, v in result.items() if v == min_val]

        return min_keys