class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curSum = 0, 0
        res = len(nums) + 1
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                curSum -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return res if res != len(nums) + 1 else 0