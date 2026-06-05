class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            tmp = max(one, two + n)
            two = one
            one = tmp
        return one