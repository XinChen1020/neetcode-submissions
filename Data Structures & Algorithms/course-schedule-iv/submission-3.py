from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # No cycles
        # For each query, whether we can reach from a -> c
        # with cache

        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
        
        @cache
        def dfs(i):

            pre = set()
            for v in adj[i]:
                pre |= {v}
                pre |= dfs(v)
                        
            return pre
        
        return [u in dfs(v) for u, v in queries]




            
            

