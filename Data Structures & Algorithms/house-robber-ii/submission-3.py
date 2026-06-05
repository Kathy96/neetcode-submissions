class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            one, two = 0, 0
            for a in arr:
                tmp = max(two, one + a)
                one = two
                two = tmp
            return two
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))