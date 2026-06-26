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

        processed = set()
        # Mark fully curr_visited node
        curr_visited = set()

        # DFS
        def dfs(curr_node, parent):
            
            # Has
            if curr_node in curr_visited:
                return False
            
            curr_visited.add(curr_node)
            processed.add(curr_node)

            for nei in adj[curr_node]:
                if nei == parent:
                    continue
                if not dfs(nei, curr_node):
                    return False
            curr_visited.remove(curr_node)
            
            return True

            

        for v in range(n):
            if v in processed:
                continue
            if not dfs(v, None):
                return False
        
        return True