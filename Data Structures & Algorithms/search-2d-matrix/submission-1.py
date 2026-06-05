class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            m = t + (b - t) // 2
            if matrix[m][-1] < target:
                t = m + 1
            elif matrix[m][0] > target:
                b = m - 1
            else:
                break
        if not t <= b:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            n = l + (r - l) // 2
            if matrix[m][n] < target:
                l = n + 1
            elif matrix[m][n] > target:
                r = n - 1
            else:
                return True
        return False 