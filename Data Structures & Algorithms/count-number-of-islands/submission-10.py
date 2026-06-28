class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
                    




        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    island += 1
        return island