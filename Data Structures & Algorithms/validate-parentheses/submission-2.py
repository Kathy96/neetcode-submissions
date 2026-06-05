class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')':'(', ']':'[', '}':'{'}
        q = []
        for c in s:
            if c in bracketMap:
                if not q or q[-1] != bracketMap[c]:
                    return False
                q.pop()
            else:
                q.append(c)
        return len(q) == 0