class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counterS1, counterS2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            counterS1[ord(s1[i]) - ord('a')] += 1
            counterS2[ord(s2[i]) - ord('a')] += 1
        
        matched = 0
        for i in range(26):
            if counterS1[i] == counterS2[i]:
                matched += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matched == 26:
                return True
            index = ord(s2[r]) - ord('a')
            counterS2[index] += 1
            if counterS1[index] == counterS2[index]:
                matched += 1
            elif counterS1[index] + 1 == counterS2[index]:
                matched -= 1
            index = ord(s2[l]) - ord('a')
            counterS2[index] -= 1
            if counterS1[index] == counterS2[index]:
                matched += 1
            elif counterS1[index] - 1 == counterS2[index]:
                matched -= 1
            l += 1
        return matched == 26