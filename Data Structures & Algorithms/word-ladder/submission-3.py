class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbor = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                neighbor[pattern].append(word)
        
        res = 1
        q = deque([beginWord])
        visited = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nei in neighbor[pattern]:
                        if nei not in visited:
                            q.append(nei)
            res += 1

        return 0