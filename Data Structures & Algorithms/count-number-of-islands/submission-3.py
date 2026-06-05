class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in seen or grid[r][c] == "0":
                return 0
            seen.add((r, c))
            for d in directions:
                dfs(r + d[0], c + d[1])
            return 1
        for i in range(ROWS):
            for j in range(COLS):
                res += dfs(i, j)
        return res