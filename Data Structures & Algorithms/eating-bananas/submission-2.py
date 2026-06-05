class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            curSum = 0
            k = l + (r - l) // 2
            for p in piles:
                curSum += math.ceil(p / k)
            if curSum <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
