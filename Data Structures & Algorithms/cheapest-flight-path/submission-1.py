class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                temp[d] = min(temp[d], prices[s] + p)
            prices = temp
        return prices[dst] if prices[dst] != float('inf') else -1