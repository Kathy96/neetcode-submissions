class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen, maxFreq = 0, 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            while r - l + 1 - k > maxFreq:
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen