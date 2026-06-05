class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)] # row, col, diff
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            diff, r, c  = heapq.heappop(minHeap)
            
            if (r, c) in visit:
                continue
            if r == ROWS -1 and c == COLS -1:
                return diff
            visit.add((r, c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR > ROWS - 1 or newC > COLS -1 or (newR, newC) in visit:
                    continue
                newDiff = max(abs(heights[r][c] - heights[newR][newC]), diff)
                heapq.heappush(minHeap, (newDiff, newR, newC))
        return 0