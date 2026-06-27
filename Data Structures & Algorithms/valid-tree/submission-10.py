class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        parents = list(range(n))
        size = [1] * n
        comp = n

        def find(node):
            
            while parents[node] != node:
            
                # Path compression for speed up in future find
                parents[node] = parents[parents[node]]
                node = parents[node]

            return parents[node]
        
        def union(component_1, component_2):
            nonlocal comp
            r1 = find(component_1)
            r2 = find(component_2)

            # If edge connecting two cluster that has the same repre,
            # there's cycle
            if r1 == r2:
                return False

            # Attach smaller cluster to bigger cluster
            if size[r1] < size[r2]:
                parents[r1] = r2
                size[r2] += size[r1]
            else:
                parents[r2] = r1
                size[r1] += size[r1]
            comp -= 1
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return comp == 1