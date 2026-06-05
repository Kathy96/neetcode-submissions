class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False

        for r in range(M):
            if matrix[r][0] == 0:
                firstColZero = True
                break
        for c in range(N):
            if matrix[0][c] == 0:
                firstRowZero = True
                break
        for r in range(M):
            if r == 0:
                continue
            for c in range(N):
                if c == 0:
                    continue
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, M):
            for c in range(1, N):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if firstColZero:
            for r in range(M):
                matrix[r][0] = 0 
        if firstRowZero:
            for c in range(N):
                matrix[0][c] = 0 
        