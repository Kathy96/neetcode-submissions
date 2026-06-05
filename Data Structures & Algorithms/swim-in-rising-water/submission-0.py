class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        visited.add ((0, 0))
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        minHeap = [[grid[0][0], 0, 0]]
        ROW, COL = len(grid), len(grid[0])
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROW-1 and c == COL - 1:
                return t
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR > ROW - 1 or newC > COL - 1 or (newR, newC) in visited:
                    continue
                visited.add((newR, newC))
                heapq.heappush(minHeap, [max(t, grid[newR][newC]), newR, newC])
    