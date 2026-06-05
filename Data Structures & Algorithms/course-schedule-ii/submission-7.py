class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visting = {}
        res = []

        def dfs(crs):
            if crs in visting:
                return visting[crs]
            visting[crs] = True
            for pre in preMap[crs]:
                if dfs(pre):
                    return True
            visting[crs] = False
            res.append(crs)
        for i in range(numCourses):
            if dfs(i):
                return []
        return res



