class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWord = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        seen = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        root = TrieNode()
        for word in words:
            root.addWord(word)
        def dfs(r, c, node, curWord):
            if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[0]) - 1 or (r, c) in seen or board[r][c] not in node.children:
                return
            node = node.children[board[r][c]]
            curWord += board[r][c]
            if node.isWord:
                res.add(curWord)
            
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, curWord)
            seen.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return list(res)