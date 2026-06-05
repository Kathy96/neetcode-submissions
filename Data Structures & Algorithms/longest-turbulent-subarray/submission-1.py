class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, sign = 1, 0
        # sign > : 1, < : -1, = : 0
        l, r = 0, 1
        while r < len(arr):
            if sign != 1 and arr[r] > arr[r - 1]:
                res = max(res, r - l + 1)
                sign = 1
                r += 1
            elif sign != -1 and arr[r] < arr[r - 1]:
                res = max(res, r - l + 1)
                sign = -1
                r += 1
            else:
                while r < len(arr) and arr[r] == arr[r - 1]:
                    r = r + 1
                sign = 0
                l = r - 1

        return res