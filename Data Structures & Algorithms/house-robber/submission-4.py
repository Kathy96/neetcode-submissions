class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            tmp = max(two, one + n)
            one = two
            two = tmp
        return two