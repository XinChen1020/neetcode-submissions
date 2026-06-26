class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree:
        # 1. Fully connected/all nodes are reachable from every other nodes
        # 2. No cycle
        
        adj = [[] for _ in range(n)]
        edge_count = 0
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            edge_count += 1
        
        # To be fully conneced, edge_count = n - 1
        if edge_count != n - 1:
            return False
        
        # Mark node in current DFS path
        curr_visited = set()

        # DFS
        # Use parent to avoid self loop in the undirected graph
        def dfs(curr_node, parent):
            
            if curr_node in curr_visited:
                return False
            
            curr_visited.add(curr_node)

            for nei in adj[curr_node]:
                if nei == parent:
                    continue
                if not dfs(nei, curr_node):
                    return False            
            return True

            
        return dfs(0, None) and len(curr_visited) == n