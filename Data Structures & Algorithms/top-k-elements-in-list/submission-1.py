class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxHeap = []
        for c in counter:
            heapq.heappush(maxHeap, (-counter[c], c))
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res