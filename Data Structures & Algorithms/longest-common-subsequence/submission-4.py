class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for _ in range(len(text2) + 1)]
        for i in range(len(text1)):
            newDp = dp.copy()
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    newDp[j + 1] = dp[j] + 1
                else:
                    newDp[j + 1] = max(dp[j + 1], newDp[j])
            dp = newDp
        return dp[len(text2)]
        