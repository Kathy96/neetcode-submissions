class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crsMap[crs] == []:
                return True
            visited.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            crsMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

