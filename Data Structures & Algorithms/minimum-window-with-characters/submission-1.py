class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        counterT = Counter(t)
        window = {}
        have, need = 0, len(counterT)
        indexArr, minLen = [-1, -1], float('inf')
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in counterT and window[c] == counterT[c]:
                have += 1
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    indexArr = [l, r]
                window[s[l]] -= 1
                if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1
        l, r = indexArr
        return s[l: r + 1] if minLen != float('inf') else ""