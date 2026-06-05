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
            t, i = heapq.heappop(minHeap)
            if i == 1:
                curMax += 1
            else:
                curMax -= 1
            res = max(curMax, res)
        return res
