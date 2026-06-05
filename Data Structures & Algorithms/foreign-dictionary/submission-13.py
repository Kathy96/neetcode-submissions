class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        wordDict = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    wordDict[w1[j]].add(w2[j])
                    break
        visited, visiting = set(), set()
        res = []
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)
            for nei in wordDict[c]:
                if not dfs(nei):
                    return False
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in wordDict:
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)