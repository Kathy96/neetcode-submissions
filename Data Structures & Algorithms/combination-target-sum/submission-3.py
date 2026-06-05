class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracking(i, curSum, curArr):
            if target == curSum:
                res.append(curArr.copy())
                return
            if i > len(nums) - 1 or curSum > target:
                return
            backTracking(i + 1, curSum, curArr)
            backTracking(i, curSum + nums[i], curArr + [nums[i]])
            
        backTracking(0, 0, [])
        return res