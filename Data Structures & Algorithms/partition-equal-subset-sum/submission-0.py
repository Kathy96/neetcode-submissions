class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        N = len(nums) - 1
        def dp(i, curSum):
            if i > N:
                return False
            if curSum == target:
                return True
            return dp(i + 1, curSum) or dp(i + 1, curSum + nums[i])

        return dp(0, 0)