class CountSquares:

    def __init__(self):
        self.counter = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.counter:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            if (px, y) in self.counter and (x, py) in self.counter:
                res += self.counter[(x, y)] * self.counter[(px, y)] * self.counter[(x, py)]
        return res
