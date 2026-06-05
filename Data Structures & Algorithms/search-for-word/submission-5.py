class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, i):
            if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[0]) - 1 or (r, c) in seen or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            seen.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            seen.remove((r, c))
            return False  
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if dfs(i, j, 0):
                    return True
        return False
