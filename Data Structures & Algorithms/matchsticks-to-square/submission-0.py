class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        sides = [0] * 4
        if totalLen % 4:
            return False
        length = totalLen // 4
        matchsticks.sort(reverse=True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                # this following line is confusing    
                if sides[j] == 0:
                    break
                
            return False
            
        return dfs(0)

