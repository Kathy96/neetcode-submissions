class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if s > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif e < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        res.append(newInterval)
        return res