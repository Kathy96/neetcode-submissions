class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minHeap = [[grid[0][0], 0, 0]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr > len(grid) - 1 or nc > len(grid[0]) - 1 or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])
                