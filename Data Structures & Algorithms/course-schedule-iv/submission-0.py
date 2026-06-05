class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        res = []
        preMap = {}

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for pre in adj[crs]:
                    preMap[crs] |= dfs(pre)
                preMap[crs].add(crs)
            return preMap[crs]

        for crs in range(numCourses):
            dfs(crs)
        
        for pre, crs in queries:
            res.append(pre in preMap[crs])
        return res