class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s >= prevEnd:
                prevEnd = e
            else:
                prevEnd = min(prevEnd, e)
                res += 1
        return res
