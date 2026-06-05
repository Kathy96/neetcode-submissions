class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        nums.sort(reverse=True)
        target = total // k
        used = [False] * len(nums)

        def backTracking(i, k, curSum):
            if k == 0:
                return True
            if curSum == target:
                return backTracking(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or curSum + nums[j] > target:
                    continue
                used[j] = True
                if backTracking(j + 1, k, curSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backTracking(0, k, 0)