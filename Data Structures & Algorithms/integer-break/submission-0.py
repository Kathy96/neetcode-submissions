class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for target in range(2, n + 1):
            dp[target] = 0 if target == n else target
            for s in range(target + 1):
                dp[target] = max(dp[target], dp[s] * dp[target - s])
        return dp[n]