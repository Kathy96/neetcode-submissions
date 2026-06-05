class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:
            adj[crs].append(pre)


        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            visited.remove(i)    
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


            