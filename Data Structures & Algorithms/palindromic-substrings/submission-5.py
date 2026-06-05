class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPali(l, r):
            cnt = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt
        for i in range(len(s)):
            res += countPali(i, i)
            res += countPali(i, i + 1)
        return res