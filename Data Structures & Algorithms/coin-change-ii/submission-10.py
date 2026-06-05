class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(1, amount + 1):
                dp[a] += dp[a - c] if c <= a else 0
        return dp[amount]