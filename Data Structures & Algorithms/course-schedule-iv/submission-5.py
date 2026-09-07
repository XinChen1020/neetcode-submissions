class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # No cycle
        # Topological sort
        # for each query, whether u before v

        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1
        
        queue = deque()
        pre = [set() for _ in range(numCourses)]

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:

            for _ in range(len(queue)):
                u = queue.popleft()
                for v in adj[u]:
                    pre[v].add(u)
                    pre[v] |= pre[u]
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

        return [u in pre[v] for u, v in queries]
                
        
