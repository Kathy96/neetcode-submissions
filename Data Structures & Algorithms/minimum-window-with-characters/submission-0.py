class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, counterT = {}, {}

        for c in t:
            counterT[c] = counterT.get(c, 0) + 1
        have, need = 0, len(counterT)

        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in counterT and window[c] == counterT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""