class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        preRow = [0 for _ in range(n)]
        for i in range(m):
            curRow = [0 for _ in range(n)]
            curRow[0] = 1
            for j in range(1, n):
                curRow[j] = curRow[j - 1] + preRow[j]
            preRow = curRow
        return preRow[n - 1]
