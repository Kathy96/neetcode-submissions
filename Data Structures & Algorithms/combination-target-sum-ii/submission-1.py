class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTracking(i, curSum, curArr):
            if curSum == target:
                res.append(curArr.copy())
                return
            if i > len(candidates) - 1 or curSum > target:
                return
            backTracking(i + 1, curSum + candidates[i], curArr + [candidates[i]])
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backTracking(i + 1, curSum, curArr)
        backTracking(0, 0, [])
        return res