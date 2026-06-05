class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in counter.items()]
        heapq.heapify(maxHeap)

        res = []
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, c = heapq.heappop(maxHeap)
            res.append(c)
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt < 0:
                prev = [cnt, c]
        return "".join(res)