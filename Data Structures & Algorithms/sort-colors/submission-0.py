class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for _ in range(3)]
        for n in nums:
            count[n] += 1
        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                index += 1
                count[i] -= 1