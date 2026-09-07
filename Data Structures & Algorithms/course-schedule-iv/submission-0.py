from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # No cycles
        # For each query, whether we can reach from a -> c
        # with cache

        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
        

        @cache
        def dfs(i, target):
            if i == target:
                return True

            
            for v in adj[i]:
                if dfs(v, target):
                    return True

            return False

        return [dfs(u, v) for u, v in queries]

            
            

