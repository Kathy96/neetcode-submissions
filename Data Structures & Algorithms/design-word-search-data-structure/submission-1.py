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
        def dfs(i, node):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in node.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.isWord
        return dfs(0, self.root)





