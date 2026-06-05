class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        while l <= r:
            m = l + (r - l) // 2
            left, cur, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            
            if left < cur < right:
                l = m + 1
            elif left > cur > right:
                r = m - 1
            else:  
                break
        peak = m

        l, r = 0, peak - 1
        while l <= r:
            m = l + (r - l) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = peak, mountainArr.length() - 1
        while l <= r:
            m = l + (r - l) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                l = m + 1
        return -1
        
