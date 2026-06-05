class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = (x**2 + y**2) 
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        output = []
        while len(maxHeap) > 0:
            (dist, x, y) = heapq.heappop(maxHeap)
            output.append([x, y])
        return output