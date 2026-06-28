class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r,c) in seen:
                return 0

            seen.add((r, c))
            for dr, dc in directions :
                dfs(r + dr, c + dc)
            return 1

        for i in range(rows):
            for j in range(cols):
                result += dfs(i, j)
        return result

