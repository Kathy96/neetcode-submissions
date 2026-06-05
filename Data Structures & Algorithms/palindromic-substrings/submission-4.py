class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPali(l, r):
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
    
        for i in range(len(s)):
            res += countPali(i, i)
            res += countPali(i, i + 1)
        return res