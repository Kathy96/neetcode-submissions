class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(i, curSum, curArr):
            if curSum == target:
                result.append(curArr.copy())
                return
            if i > len(nums) - 1 or curSum > target:
                return
            curArr.append(nums[i])
            curSum += nums[i]
            helper(i, curSum, curArr)
            curSum -= nums[i]
            curArr.pop()
            helper(i + 1, curSum, curArr)
        helper(0, 0, [])
        return result