class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = isPalindrome(i, i)
            l2, r2 = isPalindrome(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
            
        return s[start: end + 1]