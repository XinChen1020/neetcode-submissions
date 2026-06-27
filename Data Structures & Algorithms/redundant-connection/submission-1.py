class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Identify the last edge that creates a cycle
        # disjoint union set

        parents = {}
        for u, v in edges:
            parents[u] = u
            parents[v] = v
        
        sizes = {k: 1 for k in parents.keys()}
        
        
        def find(node):
            
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        result = [-1, -1]
        def union(u, v):
            nonlocal result
            r1 = find(u)
            r2 = find(v)
            if r1 == r2:
                result = [u, v]
            
            if sizes[r1] > sizes[r2]:
                parents[r2] = parents[r1]
                sizes[r1] += sizes[r2]
            else:
                parents[r1] = parents[r2]
                sizes[r2] += sizes[r1]
        
        for u, v in edges:
            union(u, v)
        
        return result
            

            

