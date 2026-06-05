class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, i):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in seen or word[i] != board[r][c]:
                return False
            if i == len(word) - 1:
                return True
            seen.add((r, c))
            for d in directions:
                if dfs(r + d[0], c + d[1], i + 1):
                    return True
            return False
        for i in range(ROWS):
            for j in range(COLS):
                seen = set()
                if dfs(i, j, 0):
                    return True
        return False