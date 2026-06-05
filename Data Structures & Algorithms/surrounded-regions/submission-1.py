class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'