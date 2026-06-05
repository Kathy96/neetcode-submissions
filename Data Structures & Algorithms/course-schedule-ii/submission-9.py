class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Input: numCourses = 3, prerequisites = [[1,0]]
        Output: [0,1,2]
        {0: [], 1: [0], 2: []}
        """
        preMap = {i:[] for i in range(numCourses)}
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
        for i in range(numCourses):
            if dfs(i):
                return []
        return output
            