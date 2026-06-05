class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        visited = set()
        edges = collections.defaultdict(list)
        for s, d, w in times:
            edges[s].append((d, w))
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1

