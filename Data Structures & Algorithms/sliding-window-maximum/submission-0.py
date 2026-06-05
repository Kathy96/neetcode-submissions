class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        l, r = 0, 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r + 1 >= k:
                l += 1
                res.append(nums[q[0]])
            r += 1

        return res