class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [[0, 0]]
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        visited = set()
        res = 0
        while len(points) > len(visited):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            for neiCost, j in adj[i]:
                if j not in visited:
                    heapq.heappush(minHeap, [neiCost, j])
        return res