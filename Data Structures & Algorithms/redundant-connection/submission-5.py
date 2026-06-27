class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Identify the first edge that creates a cycle
        # disjoint union set

        parents = [i for i in range(len(edges) + 1)]
        sizes = [1 for _ in range(len(parents))]
        
        
        def find(node):
            
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def union(u, v):
            r1 = find(u)
            r2 = find(v)
            if r1 == r2:
                return False
            
            if sizes[r1] > sizes[r2]:
                parents[r2] = parents[r1]
                sizes[r1] += sizes[r2]
            else:
                parents[r1] = parents[r2]
                sizes[r2] += sizes[r1]
            return True
            
        for u, v in edges:
            if not union(u, v):
                return [u,v]
        
            

            

