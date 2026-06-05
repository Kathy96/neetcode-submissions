class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbors[pattern].append(word)
        q = deque([beginWord])
        visited = set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in neighbors[pattern]:
                        if nei not in visited:
                            q.append(nei)
            res += 1
        return 0

