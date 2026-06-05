class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = ["X","X","Y","Y"], n = 2
        """
        count = {}
        for ch in tasks:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        """
        maxHeap = [-2, -2]

        q = [[-cnt, idleTime]]
        """
        
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time





