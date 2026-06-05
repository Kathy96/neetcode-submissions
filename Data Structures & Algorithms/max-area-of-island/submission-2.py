class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curArea = self.dfs(grid, r, c)
                maxArea = max(curArea, maxArea)
        return maxArea
    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or grid[r][c] == 0 or (r, c) in self.visited:
            return 0
        self.visited.add((r, c))
        return 1 + self.dfs(grid, r + 1, c) + self.dfs(grid, r - 1, c) + self.dfs(grid, r, c + 1) + self.dfs(grid, r, c - 1)

[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]