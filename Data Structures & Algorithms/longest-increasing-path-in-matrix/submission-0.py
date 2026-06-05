class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        dp = {}
        def dfs(r, c, preVal):
            if r < 0 or c < 0 or r > len(matrix) - 1 or c > len(matrix[0]) - 1 or matrix[r][c] <= preVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            curLen = 1
            for dr, dc in directions:
                curLen = max(curLen, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[(r, c)] = curLen
            return curLen
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        return max(dp.values())