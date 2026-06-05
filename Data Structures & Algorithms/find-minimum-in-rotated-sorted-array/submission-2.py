class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]  # Initialize with the first element

        while left <= right:
            # If the current portion is already sorted, return the leftmost element
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            mid = (left + right) // 2
            result = min(result, nums[mid])
            
            if nums[mid] >= nums[left]:
                # The left side is sorted, move to the right half
                left = mid + 1
            else:
                # The right side is unsorted, move to the left half
                right = mid - 1

        return result