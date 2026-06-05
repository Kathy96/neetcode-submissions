class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            curDay, curCap = 1, 0
            for w in weights:
                if curCap + w > cap:
                    curDay += 1
                    if curDay > days:
                        return False
                    curCap = 0

                curCap += w
            return True

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res
