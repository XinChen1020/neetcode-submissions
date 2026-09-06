from functools import cache
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        
        visited = set()

        @cache
        def dfs(i):

            if i in visited:
                return False

            visited.add(i)
            for c in adj[i]:
                if not dfs(c):
                    return False
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True