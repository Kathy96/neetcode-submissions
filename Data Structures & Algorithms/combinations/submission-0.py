class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curArr):
            if len(curArr) == k:
                res.append(curArr.copy())
                return
            if i > n:
                return
            dfs(i + 1, curArr + [i])
            dfs(i + 1, curArr)
        dfs(1, [])
        return res