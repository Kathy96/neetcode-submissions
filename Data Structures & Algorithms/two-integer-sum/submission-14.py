class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # nums = [3,4,5,6], target = 7
        # remaining = 4
        # dic = {}
        ## {n: i}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in dic:
                return [dic[remaining], i]
            else:
                dic[nums[i]] = i
        