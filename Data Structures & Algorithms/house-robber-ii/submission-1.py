class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        def helper(lis):
            rob1, rob2 = 0, 0
            for n in lis:
                tmp = max(rob2, rob1 + n)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(helper(nums[1:]), helper(nums[:-1]))