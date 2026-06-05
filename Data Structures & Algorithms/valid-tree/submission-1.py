class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {i:[] for i in range(n)}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        visited = set()
        def dfs(n, prevNode):
            if n in visited:
                return False
            visited.add(n)
            for nei in neighbors[n]:
                if nei == prevNode:
                    continue
                if not dfs(nei, n):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)
            