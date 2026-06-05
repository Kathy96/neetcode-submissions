class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap, res = [], []
        for cnt, char in ([(-a, 'a'), (-b, 'b'), (-c, 'c')]):
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, char))
        
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == c:
                if not maxHeap:
                    break
                cnt2, c2 = heapq.heappop(maxHeap)
                res.append(c2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(maxHeap, (cnt2, c2))
                heapq.heappush(maxHeap, (cnt, c))

            else:
                res.append(c)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, (cnt, c))

        return "".join(res)
