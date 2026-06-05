class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in nums:
            if (n - 1) not in numSet:
                curLen = 0
                while n in numSet:
                    curLen += 1
                    n += 1
                maxLen = max(maxLen, curLen)
        return maxLen