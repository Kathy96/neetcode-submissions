class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curSum, curArr):
            if curSum == target:
                res.append(curArr.copy())
                return
            if i == len(candidates) or curSum > target:
                return
            curArr.append(candidates[i])
            dfs(i + 1, curSum + candidates[i], curArr)
            curArr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSum, curArr)
        dfs(0, 0, [])
        return res