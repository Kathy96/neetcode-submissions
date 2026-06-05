class PrefixNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur.children:
                cur.children[w] = PrefixNode()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if not w in cur.children:
                return False
            cur = cur.children[w]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if not w in cur.children:
                return False
            cur = cur.children[w]
        return True
        