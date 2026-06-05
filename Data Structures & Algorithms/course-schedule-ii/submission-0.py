class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        res = []
        visited = set()
        cycle = set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res