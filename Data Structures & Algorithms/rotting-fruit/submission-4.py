class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        if fresh == 0:
            return 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()  
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newC < 0 or newR > len(grid) - 1 or newC > len(grid[0]) - 1 or grid[newR][newC] != 1:
                        continue
                    grid[newR][newC] = 2
                    fresh -= 1
                    q.append((newR, newC))
            time += 1
            if fresh == 0:
                return time
                
        return -1