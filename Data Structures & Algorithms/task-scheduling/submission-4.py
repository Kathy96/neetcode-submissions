class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = ["A","A","A","B","C"], n = 3
        maxHeap = [-3, -1, -1], n = 3

        """
        count = {}
        for ch in tasks:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        """
         maxHeap = [-3, -1, -1], n = 3
         [-cnt, idleTime]
         time = 1
         q = [-2]
         A
        """
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time





