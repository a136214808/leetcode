'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]
        size = len(heights)

        area = 0

        stack = [0]

        for i in range(1,size):
            while heights[i]< heights[stack[-1]]:
                s_height = heights[stack.pop()]
                s_size = i - stack[-1] -1
                area = max(area,s_size*s_height)
            stack.append(i)

        return area
