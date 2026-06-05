class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}
        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            elif rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            return 1
        res = n
        for e1, e2 in edges:
            res -= union(e1, e2)
        return res