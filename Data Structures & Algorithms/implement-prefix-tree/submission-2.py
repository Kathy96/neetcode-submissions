class PrefixNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = PrefixNode()
            curr = curr.children[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True

        
        