class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        unrottenCount = 0
        visited = set()
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    unrottenCount += 1
        if unrottenCount == 0:
            return 0
        while rotten:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr > ROWS - 1 or c + dc > COLS - 1 or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 0:
                        continue
                    visited.add((r + dr, c + dc))
                    rotten.append((r + dr, c + dc))
                    unrottenCount -= 1
            time += 1
            if unrottenCount == 0:
                return time
        return -1
