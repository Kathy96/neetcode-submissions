class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, curArr):
            if i == len(nums):
                res.append(curArr.copy())
                return
            curArr.append(nums[i])
            helper(i + 1, curArr)
            curArr.pop()
            helper(i + 1, curArr)
        helper(0, [])
        return res