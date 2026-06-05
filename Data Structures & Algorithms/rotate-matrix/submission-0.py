class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]
                #bottomLeft -> topleft
                matrix[top][l + i] = matrix[bottom - i][l]
                #bottomRight -> bottomLeft
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #topRight -> bottomRight
                matrix[bottom][r - i] = matrix[top + i][r]
                #topRight = topleft
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1