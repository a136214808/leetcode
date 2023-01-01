'''
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.
'''
from typing import List
matrix= [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]):
        maxArea = 0
        heights=[0 for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    heights[col] +=1
                else:
                    heights[col] = 0
            maxArea = max(maxArea,self.largestRectangleArea(heights))

        return maxArea

    def largestRectangleArea(self,heights):

        area = 0

        heights = [0]+heights+[0]
        n = len(heights)

        stack = [0]


        for i in range(1,n):
            while heights[i]< heights[stack[-1]]:
                s_height = heights[stack.pop()]
                s_size = i - stack[-1] -1
                area = max(area,s_size*s_height)
            stack.append(i)
        return area

        # heights = [0] + heights + [0]
        # size = len(heights)
        #
        # area = 0
        #
        # stack = [0]
        #
        # for i in range(1, size):
        #     while heights[i] < heights[stack[-1]]:
        #         s_height = heights[stack.pop()]
        #         s_size = i - stack[-1] - 1
        #         area = max(area, s_size * s_height)
        #     stack.append(i)
        #
        # return area

a = Solution()
print(a.maximalRectangle(matrix))


