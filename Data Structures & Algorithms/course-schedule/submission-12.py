class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        visited = set()

        def dfs(curr_course):
            if curr_course in visited:
                return False
            
            if curr_course not in pre_map:
                return True
            
            visited.add(curr_course)

            for pre in pre_map[curr_course]:
                if not dfs(pre):
                    return False
            visited.remove(curr_course)
            # prune 
            pre_map[curr_course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True