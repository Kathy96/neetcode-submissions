class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isalpha() and not s[L].isdigit():
                L += 1
            while L < R and not s[R].isalpha() and not s[R].isdigit():
                R -= 1 
            if s[L].upper() != s[R].upper():
                return False
            L += 1
            R -= 1
        return True