class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        
        for n in nums:
            next_dp = defaultdict(int)
            for curSum, count in dp.items():
                next_dp[curSum + n] += count
                next_dp[curSum - n] += count
            dp = next_dp
        
        return dp[target]