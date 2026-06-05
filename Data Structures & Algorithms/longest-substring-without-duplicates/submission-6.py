class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "zxyzxyz"
             l
                r
        set (z, x, y)
        """
        l = 0
        ch_set = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in ch_set:
                ch_set.remove(s[l])
                l += 1
            ch_set.add(s[r])
            max_len = max(max_len, len(ch_set))
        return max_len

