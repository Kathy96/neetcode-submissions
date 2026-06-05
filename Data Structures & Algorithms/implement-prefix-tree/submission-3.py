class PrefixNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = PrefixNode()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True
        
        