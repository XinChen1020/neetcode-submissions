from functools import cache

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS 
        # Add each cell that reach the boarder to the result
        results = []
        search_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = {}

        def dfs(i, j)-> tuple[bool, bool]:
            pacific, atlantic = False, False
            temp = heights[i][j]
            heights[i][j] = 100000
            
            for d in search_dir:
                new_i = i + d[0]
                new_j = j + d[1]

                # Touch the ocean
                if new_i < 0 or new_j < 0:
                    pacific = True
                    continue
                if new_i >= len(heights) or new_j >= len(heights[0]):
                    atlantic = True
                    continue

                if temp >= heights[new_i][new_j]:
                    if (new_i, new_j) in visited:
                        new_p, new_a = visited[(new_i, new_j)]
                    else:
                        new_p, new_a = dfs(new_i, new_j)
                    pacific, atlantic = pacific or new_p, atlantic or new_a
            
            visited[(i, j)] = (pacific, atlantic)
            
            heights[i][j] = temp

            
            return pacific, atlantic
            
                
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                p, a = dfs(i, j)
                
                if p and a:
                    results.append([i, j])
        
        return results
