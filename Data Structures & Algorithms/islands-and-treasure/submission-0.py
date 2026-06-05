class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS  = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        dist = 0
        direction = [[0, 1], [0, -1], [1, 0],[-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or (r, c) in visited or grid[r][c] == -1:
                    continue
                visited.add((r, c))
                grid[r][c] = dist
                for dr, dc in direction:
                    q.append((r + dr, c + dc))

            dist += 1