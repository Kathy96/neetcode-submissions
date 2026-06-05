class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        adj = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        res = 0
        visited = set()
        minHeap = [[0, 0]]
        while len(points) > len(visited):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            for j, neiCost in adj[i]:
                if j not in visited:
                    heapq.heappush(minHeap,[neiCost, j])
        return res
            