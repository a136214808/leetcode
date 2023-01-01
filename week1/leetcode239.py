'''
239. Sliding Window Maximum

You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
'''
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self,nums:List[int],k:int)->List[int]:
        n = len(nums)
        #双端队列(存储元素下标)
        q = collections.deque()
        #存放最大值
        res=[]

        if k<1:
            return res

        #构建窗口
        for i in range(k):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])

        #开始寻找
        for i in range(k,n):
            while q and q[0] <= i-k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            res.append(nums[q[0]])

        return res
