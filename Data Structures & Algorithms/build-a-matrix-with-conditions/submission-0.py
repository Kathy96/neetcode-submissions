class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            visiting = set()
            visited = set()
            order = []
            adj = defaultdict(list)
            
            def dfs(src):
                if src in visiting:
                    return False
                if src in visited:
                    return True
                visited.add(src)
                visiting.add(src)
                for nei in adj[src]:
                    if not dfs(nei):
                        return False
                visiting.remove(src)
                order.append(src)
                return True
            for src, dst in edges:
                adj[src].append(dst)
            for src in range(1, k + 1):
                if src not in visited:
                    if not dfs(src):
                        return []
            return order[::-1]

        row_order = topo_sort(rowConditions)
        if not row_order:
            return []
        col_order = topo_sort(colConditions)
        if not col_order:
            return []
        
        val_to_row = {n : i for i, n in enumerate(row_order)}
        val_to_col = {n : i for i, n in enumerate(col_order)}
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            r, c = val_to_row[i], val_to_col[i]
            res[r][c] = i
        return res

