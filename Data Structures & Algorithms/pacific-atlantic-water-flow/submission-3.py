class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, preHeight, visited):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or (r, c) in visited or heights[r][c] < preHeight:
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visited)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
            