class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        nei = defaultdict(list)
        visited = set()
        for u, v, t in times:
            nei[u].append((v, t))
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in visited:
                continue
            visited.add(u1)
            time = t1
            for u2, t2 in nei[u1]:
                if u2 not in visited:
                    heapq.heappush(minHeap, (t1 + t2, u2))
        return time if len(visited) == n else -1