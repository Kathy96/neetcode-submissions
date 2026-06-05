class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newC < 0 or newR > ROWS - 1 or newC > COLS -1 or grid[newR][newC] != 1:
                        continue
                    q.append((newR, newC))
                    grid[newR][newC] = 2
                    fresh -= 1
            time += 1
            if fresh == 0:
                return time
        return -1
