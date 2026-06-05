class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(len(s)):
            l, r = isPalindrome(i, i)
            if r - l > end - start:
                start, end = l, r
            l, r = isPalindrome(i, i + 1)
            if r - l > end - start:
                start, end = l, r
            
        return s[start: end + 1]