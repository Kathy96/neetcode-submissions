class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [0, 0]
        for n in nums:
            tmp = houses[0]
            houses[0] = max(houses[0], houses[1] + n)
            houses[1] = tmp
        return houses[0]
