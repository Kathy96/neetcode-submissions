class TrieNode():

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
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        seen = set()
        res = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, node, curWord):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or board[r][c] not in node.children:
                return
            curWord += board[r][c]
            seen.add((r, c))
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(curWord)
            
            for d in directions:
                dfs(r + d[0], c + d[1], node, curWord)
            seen.remove((r, c))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        return list(res)
            