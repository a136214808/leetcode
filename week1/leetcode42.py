'''
42. Trapping Rain Water

non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        #计算面积
        res = 0

        height = height + [0]

        n = len(height)

        stack=[0]

        for i in range(n):
            #新进入的 比 顶层的 小
            if height[i]<=height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i]>=height[stack[-1]]:
                    bottom = stack.pop()
                    if stack:
                        h = min(height[i],height[stack[-1]])-height[bottom]
                        w = i - stack[-1] - 1
                        res += h*w
                stack.append(i)
        return res

a = Solution()
print(a.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))


