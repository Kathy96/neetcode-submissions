class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                maxArea = max(maxArea, (i - prevI) * prevH)
                start = prevI
            stack.append([start, h])
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea