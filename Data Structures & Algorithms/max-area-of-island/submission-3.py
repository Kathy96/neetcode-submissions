class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curArea = dfs(grid, r, c)
                maxArea = max(curArea, maxArea)
        return maxArea
    
