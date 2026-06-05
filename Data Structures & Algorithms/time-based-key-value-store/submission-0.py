class TimeMap:

    def __init__(self):
        self.timeMap = {} # key=key, value=[[timestamp, value]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
