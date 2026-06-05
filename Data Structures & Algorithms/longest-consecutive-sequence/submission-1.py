class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for n in nums:
            if (n - 1) not in numSet:
                cur = 0
                while n in numSet:
                    cur += 1
                    n += 1
                if cur > res:
                    res = cur
        return res