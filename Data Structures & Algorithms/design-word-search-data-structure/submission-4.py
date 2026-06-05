class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(cur, i):
            for j in range(i, len(word)):
                w = word[j]
                if w == '.':
                    for v in cur.children.values():
                        if dfs(v, j + 1):
                            return True
                    return False
                else:
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
            return cur.isWord
        return dfs(self.root, 0)
