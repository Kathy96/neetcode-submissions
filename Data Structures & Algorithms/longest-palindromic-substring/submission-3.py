class Solution:
    def longestPalindrome(self, s: str) -> str:
        startIdx = 0
        minLen = 0
        def isPalindrome(l, r):
            nonlocal startIdx
            nonlocal minLen

            while l >= 0 and r <= len(s) -1 and s[l] == s[r]:
                if r - l + 1 > minLen:
                    startIdx = l
                    minLen = r - l + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i + 1)
        
        return "".join(s[startIdx: startIdx + minLen])