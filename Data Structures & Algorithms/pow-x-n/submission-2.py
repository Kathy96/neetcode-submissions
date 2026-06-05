class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                n -= 1
                res *= x 
        return res
