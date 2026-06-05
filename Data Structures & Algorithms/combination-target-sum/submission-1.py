class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, curSum, curArr):
            if curSum == target:
                res.append(curArr.copy())
                return
            if i == len(nums) or curSum > target:
                return
            curArr.append(nums[i])
            helper(i, curSum + nums[i], curArr)
            curArr.pop()
            helper(i + 1, curSum, curArr)
        helper(0, 0, [])
        return res