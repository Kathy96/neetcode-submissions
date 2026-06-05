class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                above = self.sumMat[r - 1][c] if r > 0 else 0
                left = self.sumMat[r][c - 1] if c > 0 else 0
                aboveLeft = self.sumMat[r - 1][c - 1] if r > 0 and c > 0 else 0
                self.sumMat[r][c] = matrix[r][c] + above + left - aboveLeft


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            above = self.sumMat[row1 - 1][col2] if row1 > 0 else 0
            left = self.sumMat[row2][col1 - 1] if col1 > 0 else 0
            aboveLeft = self.sumMat[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
            return self.sumMat[row2][col2] - above - left + aboveLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
[3, 0, 1, 4, 2]
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], 
[1, 0, 3, 0, 5]