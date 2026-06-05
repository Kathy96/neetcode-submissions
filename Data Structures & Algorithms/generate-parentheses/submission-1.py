class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backTracking(openN, closeN):
            if openN == n and closeN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backTracking(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backTracking(openN, closeN + 1)
                stack.pop()
        backTracking(0, 0)
        return res