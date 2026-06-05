class Solution:
    def isValid(self, s: str) -> bool:
        bracketDic = {']':'[', ')':'(', '}':'{'}
        stack = []
        for c in s:
            if c in bracketDic:
                if not stack:
                    return False
                elif stack[-1] != bracketDic[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0