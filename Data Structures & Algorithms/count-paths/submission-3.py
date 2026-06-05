class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        for i in range(m - 1):
            newRow = [1 for _ in range(n)]
            for j in range(n - 2, -1, -1):    
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]