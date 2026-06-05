class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            curSum = 0
            tmp = n
            while tmp:
                digit = tmp % 10
                curSum += digit ** 2
                tmp //= 10
            n = curSum
            if n == 1:
                return True

        return False