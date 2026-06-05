class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backTrack(i, curSum, k):
            if k == 0:
                return True
            if curSum == target:
                return backTrack(0, 0, k - 1)
            prev = -1
            for j in range(i, len(nums)):
                if used[j] or curSum + nums[j] > target:
                    continue
                if nums[j] == prev:
                    continue
                used[j] = True
                if backTrack(j + 1, curSum + nums[j], k):
                    return True
                used[j] = False
                prev = nums[j]
            return False
        return backTrack(0, 0, k)