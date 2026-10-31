class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights + [0]):
            start = i
            
            while stack and stack[-1][1] > height:
                index, h = stack.pop()

                area = h*(i - index)
                max_area = max(area, max_area)

                start = index

            stack.append((start, height))
        return max_area