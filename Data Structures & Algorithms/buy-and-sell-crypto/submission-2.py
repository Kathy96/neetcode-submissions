class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            curProfit = p - minPrice
            maxProfit = max(maxProfit, curProfit)
            minPrice = min(minPrice, p)
        return maxProfit