"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        for interval in intervals:
            heapq.heappush(minHeap, (interval.start, 1))
            heapq.heappush(minHeap, (interval.end, -1))
        res, curMax = 0, 0
        while minHeap:
            t, count = heapq.heappop(minHeap)
            curMax += count
            res = max(curMax, res)
        return res
