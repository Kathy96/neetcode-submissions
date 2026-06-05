class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDic = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courseDic[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if courseDic[crs] == []:
                return True
            visited.add(crs)
            for pre in courseDic[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            courseDic[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

