class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxHeap = []
        for c in counter:
            heapq.heappush(maxHeap, (-counter[c], c))
        a = 1
        res = []
        while a <= k:
            freq, c = heapq.heappop(maxHeap)
            res.append(c)
            a += 1
        return res