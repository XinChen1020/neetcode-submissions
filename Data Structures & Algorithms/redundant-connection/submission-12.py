class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS

        # Create adj 
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        # Store what's in cycle
        cycle = set()
        # Marker for when does cycle start so we can start tracking cycle nodes
        cycle_start = -1
        # need to parent to distinguich cycle and going backward
        def dfs(node, parent):
            nonlocal cycle_start
            if node in visited:
                cycle_start = node
                cycle.add(node)
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if dfs(nei, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True
            return False
        
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []


