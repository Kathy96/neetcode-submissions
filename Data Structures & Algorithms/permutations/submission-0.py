class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTracking(i):
            if i == len(nums):
                return [[]]
            result = []
            prePerm = backTracking(i + 1)
            for p in prePerm:
                for j in range(len(p) + 1):
                    copyP = p.copy()
                    copyP.insert(j, nums[i])
                    result.append(copyP)
            return result
        return backTracking(0)
