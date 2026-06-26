class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort
        # pre -> course 
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # calculate indegree and adj 
        for course, preq in prerequisites:
            indegree[course] += 1
            adj[preq].append(course)

        # DFS version
        res = []
        def dfs(curr_node):
            res.append(curr_node)

            # Marker so node wouldn't get reprocessed
            indegree[curr_node] -= 1

            for n in adj[curr_node]:
                indegree[n] -=1
                if indegree[n] == 0:
                    dfs(n)

        # Do DFS for all node with 0 n 
        for n in range(numCourses):
            if indegree[n] == 0:
                dfs(n)
        
        return res if len(res) == numCourses else []