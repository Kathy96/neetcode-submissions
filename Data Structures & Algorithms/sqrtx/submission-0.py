class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = x
        while l <= r:
            m = l + (r - l) // 2
            m_square = m ** 2
            if m_square == x:
                return m
            elif m_square < x:
                l = m + 1
                res = m
            else:
                r = m - 1
        return res