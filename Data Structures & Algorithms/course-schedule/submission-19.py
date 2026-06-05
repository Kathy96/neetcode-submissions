class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = {}
        output = []

        def dfs(crs):
            if crs in visiting:
                return visiting[crs]
            visiting[crs] = True

            for pre in preMap[crs]:
                if dfs(pre):
                    return True
            visiting[crs] = False
            output.append(crs)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True