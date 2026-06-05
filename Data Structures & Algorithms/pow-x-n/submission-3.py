class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        
        while n:
            if n % 2 == 0:
                n //= 2
                x *= x
            else:
                n -= 1
                res *= x
        return res