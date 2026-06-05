class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1, 1]

        for i in range(n - 1):
            temp = stairs[0]
            stairs[0] = stairs[0] + stairs[1]
            stairs[1] = temp
        return stairs[0]