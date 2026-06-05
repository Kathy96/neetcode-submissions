class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = {}
        res = []

        def dfs(crs):
            if crs in visited:
                return visited[crs]
            visited[crs] = True
            for pre in preMap[crs]:
                if dfs(pre):
                    return True
            visited[crs] = False
            res.append(crs)
        for i in range(numCourses):
            if dfs(i):
                return False
        return True