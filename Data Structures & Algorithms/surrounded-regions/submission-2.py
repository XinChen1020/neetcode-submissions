class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # bfs
        # go from boarder and mark all cells as safe ("S")
        # Then fill are surrounded unsafe 'O'

        SAFE = "S"
        queue = deque()
        r, c = len(board), len(board[0])
        search_d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Fill in queue
        for i in range(r):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][c - 1] == "O":
                queue.append((i, c - 1))
        
        for j in range(c):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[r - 1][j] == "O":
                queue.append((r - 1, j))

        # BFS
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "O":
                board[i][j] = SAFE
                for d in search_d:
                    new_i = i + d[0]
                    new_j = j + d[1]

                    if 0 < new_i < r and 0 < new_j < c:
                        queue.append((new_i, new_j))

        # Filling
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                # Revert back
                elif board[i][j] == SAFE:
                    board[i][j] = "O"


