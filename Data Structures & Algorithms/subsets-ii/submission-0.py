class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, curArr):
            if i == len(nums):
                res.append(curArr.copy())
                return
            curArr.append(nums[i])
            backtrack(i + 1, curArr)
            curArr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curArr)
        backtrack(0, [])
        return res