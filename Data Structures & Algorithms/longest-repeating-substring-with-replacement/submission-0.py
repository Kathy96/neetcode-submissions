class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        result = 0
        maxf = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxf = max(maxf, count[s[R]])
            while R - L + 1 - maxf > k:
                count[s[L]] -= 1
                L += 1
            result = max(R - L + 1, result)
        return result