class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res