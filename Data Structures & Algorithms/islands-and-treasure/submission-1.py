class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS  = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0
        direction = [[0, 1], [0, -1], [1, 0],[-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = dist
                for dr, dc in direction:
                    if r + dr < 0 or c + dc < 0 or r + dr > ROWS - 1 or c + dc > COLS - 1 or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == -1:
                        continue
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            dist += 1