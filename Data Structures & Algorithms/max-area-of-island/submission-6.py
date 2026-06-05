class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxIsland = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        """
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]


        """

        def bfs(r, c):
            island = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1):
                        island += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return island


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxIsland = max(bfs(i, j), maxIsland)
        return maxIsland

        