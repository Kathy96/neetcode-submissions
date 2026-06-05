class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        counterT, window = Counter(t), {}
        l = 0
        have, need = 0, len(counterT)
        idxArr, minLen = [-1, -1], float('inf')
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in counterT and window[c] == counterT[c]:
                have += 1
            while have == need:
                if r - l + 1 < minLen:
                    idxArr, minLen = [l, r], r - l + 1
                window[s[l]] -= 1
                if s[l] in counterT and window[s[l]] + 1 == counterT[s[l]]:
                    have -= 1
                l += 1
        l, r = idxArr
        return s[l:r + 1] if minLen != float('inf') else ""