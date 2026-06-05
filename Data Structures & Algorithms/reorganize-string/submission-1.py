class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in counter.items()]
        heapq.heapify(maxHeap)

        res = []
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(res) > 0 and res[-1] == c:
                if not maxHeap:
                    return ""
                cnt2, c2 = heapq.heappop(maxHeap)
                res.append(c2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(maxHeap, [cnt2, c2])
                heapq.heappush(maxHeap, [cnt, c])
            else:
                res.append(c)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, [cnt, c])
            
            
        return "".join(res)