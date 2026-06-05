class MedianFinder:

    def __init__(self):
        self.smallMaxHeap, self.largeMinHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallMaxHeap, -1 * num)
        if self.smallMaxHeap and self.largeMinHeap and -1 * self.smallMaxHeap[0] > self.largeMinHeap[0]:
            val = -1 * heapq.heappop(self.smallMaxHeap)
            heapq.heappush(self.largeMinHeap, val)
        if len(self.smallMaxHeap) > len(self.largeMinHeap) + 1:
            val = -1 * heapq.heappop(self.smallMaxHeap)
            heapq.heappush(self.largeMinHeap, val)
        if len(self.largeMinHeap) > len(self.smallMaxHeap) + 1:
            val = heapq.heappop(self.largeMinHeap)
            heapq.heappush(self.smallMaxHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.smallMaxHeap) > len(self.largeMinHeap):
            return -1 * self.smallMaxHeap[0]
        elif len(self.smallMaxHeap) < len(self.largeMinHeap):
            return self.largeMinHeap[0]
        else:
            return (-1 * self.smallMaxHeap[0] + self.largeMinHeap[0]) / 2
        