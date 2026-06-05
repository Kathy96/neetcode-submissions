class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        res = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, node, curWord):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or board[r][c] not in node.children or (r, c) in seen:
                return
            curWord += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(curWord)
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, curWord)
            seen.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
        








