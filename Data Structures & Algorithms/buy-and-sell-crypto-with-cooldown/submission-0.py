class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in dp:
                return dp[(i, isBuy)]
            cooldown = dfs(i + 1, isBuy)
            if isBuy:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, isBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, isBuy)] = max(sell, cooldown)
            return dp[(i, isBuy)]
        return dfs(0, True)
