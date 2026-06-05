class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        wordDict = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    wordDict[word1[j]].add(word2[j])
                    break
        res = []
        visited = {}
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in wordDict[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)

        for w in wordDict:
            if dfs(w):
                return ""
        res.reverse()

        return "".join(res)