class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = math.ceil(total / 2)
        def dfs(i, curSum):
            if curSum >= target or i >= len(stones):
                return abs(curSum - (total - curSum))
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            dp[(i, curSum)] = min(dfs(i + 1, curSum), dfs(i + 1, curSum + stones[i]))
            return dp[(i, curSum)]
        dp = {}
        return dfs(0, 0)