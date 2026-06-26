class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn algo
        # Build indegree
        # if pre of a course, pre -> course
        indegree = [0] * numCourses
        # adj[i] hold nodes that i -> n
        adj = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            indegree[course] += 1
            adj[pre].append(course)
        
        # Add all 0 indegree node to the queue
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        # Processing by removing node with 0 indegree
        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1
            for n in adj[node]:
                indegree[n] -= 1

                if indegree[n] == 0:
                    queue.append(n)
        # If there's cycle, there will be node that couldn't be
        # processed since it would never have indegree 0
        return processed == numCourses