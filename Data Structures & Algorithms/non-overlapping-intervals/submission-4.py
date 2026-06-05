class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        preEnd = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s >= preEnd:
                preEnd = e
            else:
                preEnd = min(e, preEnd)
                res += 1
        return res