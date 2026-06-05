class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            globalMax = max(curMax, globalMax)
            globalMin = min(curMin, globalMin)
            total += n
        if globalMax < 0:
            return globalMax
        else:
            return max(globalMax, total - globalMin)