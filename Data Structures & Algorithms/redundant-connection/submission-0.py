class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {i: i for i in range(1, len(edges) + 1)}
        rank = {i: 0 for i in range(1, len(edges) + 1)}
        def find(n):
            while n != par[n]:
                n = par[n]
            return n
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                rank[p2] += 1
                par[p1] = p2
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

            
