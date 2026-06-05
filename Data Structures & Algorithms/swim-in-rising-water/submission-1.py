class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        visited.add((0, 0))
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [[grid[0][0], 0, 0]]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in direction:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR > ROWS - 1 or newC > COLS - 1 or (newR, newC) in visited:
                    continue
                visited.add((newR, newC))
                heapq.heappush(minHeap, [max(t, grid[newR][newC]), newR, newC])
