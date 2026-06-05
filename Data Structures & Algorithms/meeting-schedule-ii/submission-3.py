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
        res, curMax = 0, 0
        for i in intervals:
            heapq.heappush(minHeap, (i.start, 1))
            heapq.heappush(minHeap, (i.end , -1))
        while minHeap:
            t, count = heapq.heappop(minHeap)
            curMax += count
            res = max(curMax, res)
        return res
