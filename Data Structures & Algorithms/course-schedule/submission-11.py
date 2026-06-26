class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        connections = defaultdict(list)

        # Create connection defaultdict
        # key = prerequisites, value = class could be taken
        for i, j in prerequisites:
            connections[j].append(i)
        
        # Use dfs to search for loop
        # Note: no slow fast pointer since a node can have multiple branchs
        def dfs():
            visited = set()
            for node in connections:
                if node in visited:
                    continue
                stack = deque([(node, set())])

                while stack:
                    pre, curr_path = stack.pop()
                    visited.add(pre)
                    for c in connections[pre]:

                        if c in curr_path:
                            return False
                        if c not in connections:
                            continue  
                        path = curr_path.copy()
                        path.add(c)
                        stack.append((c, path))
            
            return True
        
        return dfs()