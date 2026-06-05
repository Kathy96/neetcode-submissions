class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / m)
            if hour <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res