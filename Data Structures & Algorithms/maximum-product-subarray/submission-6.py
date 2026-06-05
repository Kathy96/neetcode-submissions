class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        for n in nums:
            temp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp * n, curMin * n, n)
            res = max(curMax, res)
        return res
