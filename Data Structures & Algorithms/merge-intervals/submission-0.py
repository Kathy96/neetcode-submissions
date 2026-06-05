class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for start, end in intervals:
            lastEnd = res[-1][1]
            if start > lastEnd:
                res.append([start, end])
            else:
                res[-1][1] = max(lastEnd, end)
        return res