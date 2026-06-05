class Solution:
    def numDistinct(self, s: str, t: str) -> int:
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