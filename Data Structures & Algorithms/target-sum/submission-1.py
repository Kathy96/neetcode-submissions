class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backTracking(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            dp[(i, curSum)] = backTracking(i + 1, curSum + nums[i]) + backTracking(i + 1, curSum - nums[i])
            return dp[(i, curSum)]
        return backTracking(0, 0)