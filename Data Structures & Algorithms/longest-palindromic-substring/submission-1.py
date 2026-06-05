class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longestLen = 0
        self.res = ""
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.longestLen:
                    self.longestLen = r - l + 1
                    self.res = s[l:r + 1]
                l -= 1
                r += 1
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        return self.res
