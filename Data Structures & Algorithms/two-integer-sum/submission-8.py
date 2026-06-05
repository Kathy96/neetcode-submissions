class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        {4:0, }
        """
        map = {}

        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            
            map[nums[i]] = i
        

        