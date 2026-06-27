class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Disjoint union set
        parents = list(range(n))
        comp = n
        sizes = [1] * n

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def union(u, v):
            nonlocal comp
            ru = find(u)
            rv = find(v)
            if ru != rv:
                comp -= 1
            if sizes[ru] > sizes[rv]:
                parents[rv] = ru
                sizes[ru] += sizes[rv]
            else:
                parents[ru] = rv
                sizes[rv] += sizes[ru]
        
        for u, v in edges:
            union(u, v)
        
        return comp
            