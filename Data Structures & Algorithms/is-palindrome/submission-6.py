class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not isAlphanumeric(s[i]):
                i += 1
            while i < j and not isAlphanumeric(s[j]):
                j -= 1
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True