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
        
        visited = set()

        # BFS
        def bfs(node):
            # use (node, parent) to prevent going backward
            queue = deque([[node, -1]])

            while queue:
                node, parent = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)
 
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    queue.append([nei , node])
            
            return True
        return bfs(0) and len(visited) == n
            