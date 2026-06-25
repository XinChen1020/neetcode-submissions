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
                curr_path = set()
                stack = deque([node])

                while stack:
                    pre = stack.pop()
                    curr_path.add(pre)
                    for c in connections[pre]:

                        if c in curr_path:
                            return False
                        if c not in connections:
                            continue
                        
                        stack.append(c)
            
            return True
        
        return dfs()