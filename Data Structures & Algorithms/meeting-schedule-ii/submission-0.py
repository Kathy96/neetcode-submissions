"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        times.sort(key=lambda time: (time[0], time[1]))

        curMax, totalMax = 0, 0
        for t in times:
            curMax += t[1]
            totalMax = max(curMax, totalMax)
        return totalMax