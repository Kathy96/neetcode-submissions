class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            remaindar = target - nums[i]
            if remaindar in map:
                return [map[remaindar], i]
            else:
                map[nums[i]] = i
        