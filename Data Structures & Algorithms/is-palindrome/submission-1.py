class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isdigit() and not s[L].isalpha():
                L += 1
            while L < R and not s[R].isdigit() and not s[R].isalpha():
                R -= 1
            if s[L].upper() != s[R].upper():
                return False
            L += 1
            R -= 1
        return True