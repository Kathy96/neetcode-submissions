class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        root = TrieNode()
        for word in words:
            root.addWord(word)
        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r + 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c - 1, word, node)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)


