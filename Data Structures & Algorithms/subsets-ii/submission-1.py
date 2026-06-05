class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backTracking(i, curArr):
            if i == len(nums):
                res.append(curArr.copy())
                return
            backTracking(i + 1, curArr + [nums[i]])
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backTracking(i + 1, curArr)
            
        backTracking(0, [])
        return res