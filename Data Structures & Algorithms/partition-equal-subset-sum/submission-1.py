class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        N = len(nums)
        dp = {}
        def helper(i, curSum):
            if i == N:
                dp[(i, curSum)] = False
                return dp[(i, curSum)]
            if curSum == target:
                dp[(i, curSum)] = True
                return dp[(i, curSum)]
            dp[(i, curSum)] = helper(i + 1, curSum) or helper(i + 1, curSum + nums[i])
            return dp[(i, curSum)]

        return helper(0, 0)