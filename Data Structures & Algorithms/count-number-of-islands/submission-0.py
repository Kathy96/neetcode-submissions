class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count += self.dfs(grid, r, c, visited)
        return count

        
    def dfs(self, grid, r, c, visited):
        if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or grid[r][c] == "0" or (r, c) in visited:
            return 0
        visited.add((r, c))
        grid[r][c] = "0"
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r, c + 1, visited)
        self.dfs(grid, r, c - 1, visited)
        return 1