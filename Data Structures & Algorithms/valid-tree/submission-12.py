class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        parents = list(range(n))
        size = [1] * n
        comp = n

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            nonlocal comp

            r1 = find(node1)
            r2 = find(node2)

            if r1 == r2:
                return False

            if size[r1] < size[r2]:
                parents[r1] = r2
                size[r2] += size[r1]
            else:
                parents[r2] = r1
                size[r1] += size[r2]

            comp -= 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return comp == 1