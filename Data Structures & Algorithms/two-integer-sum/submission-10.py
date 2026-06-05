class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        {4:0, }
        """
        map = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in map:
                return [map[remain], i]
            map[nums[i]] = i

        