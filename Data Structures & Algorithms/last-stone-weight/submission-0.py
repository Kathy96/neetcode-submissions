class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1 :
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return abs(heapq.heappop(stones))