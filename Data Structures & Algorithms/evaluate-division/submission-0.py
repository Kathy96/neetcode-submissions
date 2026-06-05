class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            visit = set()
            q = deque([(src, 1)])
            visit.add(src)

            while q:
                cur, w = q.popleft()
                if cur == target:
                    return w
                for nei, weight in adj[cur]:
                    if nei not in visit:
                        q.append((nei, weight * w))
                        visit.add(nei)
            return -1

        return [bfs(a, b) for a, b in queries]
            