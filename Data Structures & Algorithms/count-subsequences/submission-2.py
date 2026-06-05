class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp = {}

        # def dfs(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if s[i] == t[j]:
        #         dp[(i, j)] = dfs(i + 1, j) + dfs(i + 1, j + 1)
        #     else:
        #         dp[(i, j)] = dfs(i + 1, j)
        #     return dp[(i, j)]
        # return dfs(0, 0)

        dp = [0] * (len(t) + 1)
        dp[len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            next_dp = dp.copy()
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    next_dp[j] = dp[j] + dp[j + 1]
                else:
                    next_dp[j] = dp[j]
            dp = next_dp.copy()
        return dp[0]