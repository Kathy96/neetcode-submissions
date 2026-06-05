class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] < nums[r]:
                res = min(res, nums[m])
                r = m
            else:
                res = min(res, nums[r])
                l = m + 1
        return res