class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0
        seen = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or (r, c) in seen or grid[r][c] == "0":
                return 0
            
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(i, j)
        return res