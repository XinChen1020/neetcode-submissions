class DisjoinSet:
    def __init__(self, points):


        self.parents = [i for i in range(points)]
        self.ranks = [0] * points
    
    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        
        return self.parents[u]
    
    def union(self, u, v) -> bool:
        u_parent = self.find(u)
        v_parent = self.find(v)

        # Cycle prevention
        if u_parent == v_parent:
            return False
        
        # Attach smaller tree to larger tree
        # Note: Rank is the max tree height possible, not the actual one
        if self.ranks[u_parent] > self.ranks[v_parent]:
            self.parents[v_parent] = u_parent
        elif self.ranks[u_parent] < self.ranks[v_parent]:
            self.parents[u_parent] = v_parent
        else:
            self.parents[v_parent] = u_parent
            self.ranks[u_parent] += 1
            
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Krushall's algorithm
        # Sort edge by lowest weight
        # Use Union find to make sure that there's no cycle forming 

        # Generate all potenial edge + weight (distance)
        edges = []
        for u in range(len(points) - 1):
            for v in range(u, len(points)):
                distance = abs(points[u][1] - points[v][1]) + abs(points[u][0] - points[v][0])
                edges.append([distance, u, v])
        
        # Sort edges by distance
        edges.sort()
        disjoin_set = DisjoinSet(len(points))

        # Get MST
        cost = 0
        for w, u, v in edges:
            if disjoin_set.union(u, v):
                cost += w
        
        return cost







