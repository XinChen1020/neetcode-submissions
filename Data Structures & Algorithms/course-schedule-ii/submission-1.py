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
        
        # Add all node with indegree = 0 to the queue
        # queue store node
        # BFS
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        # Prcess indegree = 0 node continusely
        finished = 0
        res = []
        while queue:
            node = queue.popleft()
            finished += 1
            res.append(node)

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        return res if finished == numCourses else []
