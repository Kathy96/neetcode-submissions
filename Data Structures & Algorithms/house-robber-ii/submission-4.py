class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            houses = [0, 0]
            for n in arr:
                tmp = max(houses[0], houses[1] + n)
                houses[1] = houses[0]
                houses[0] = tmp
            return houses[0]
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))