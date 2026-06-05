class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        result = 0
        while L < R:
            left, right = heights[L], heights[R]
            if left < right:
                result = max(result, (R - L) * left)
                L += 1                
            else:
                result = max(result, (R - L) * right)
                R -= 1                            
        return result