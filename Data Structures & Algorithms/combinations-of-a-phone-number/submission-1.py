class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}    
        result = []
        def helper(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for c in digitMap[digits[i]]:
                helper(i + 1, curStr + c)
        
        helper(0, "")
        return result