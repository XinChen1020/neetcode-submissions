class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Flow water into cells
        # dfs

        r_count, c_count = len(heights), len(heights[0])
        search_d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prev_h):
            if (i, j) in visited or \
            i < 0 or j < 0 or i == r_count or j == c_count or \
            heights[i][j] < prev_h:
                return
            
            visited.add((i, j))

            for d in search_d:
                dfs(i + d[0], j + d[1], visited, heights[i][j])
        
        # Top + down boundaries
        for j in range(c_count):
            dfs(0, j, pacific, heights[0][j])
            dfs(r_count - 1, j, atlantic, heights[r_count - 1][j])
        
        # Left + right boundaries
        for i in range(r_count):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, c_count - 1, atlantic, heights[i][c_count - 1])
        
        return list(pacific & atlantic)


