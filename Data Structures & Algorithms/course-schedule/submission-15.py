class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        def hasCycle(crs):
            if crs in visiting:
                return True
            if preMap[crs] == []:
                return False
            visiting.add(crs)
            for pre in preMap[crs]:
                if hasCycle(pre):
                    return True
            visiting.remove(crs)
            preMap[crs] = []
            return False
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True