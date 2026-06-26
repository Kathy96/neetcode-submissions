class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for n in nums:
            if n in numset:
                return True
            else:
                numset.add(n)
        return False


        time: O(n)
        space: O(n)