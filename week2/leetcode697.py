'''
697. Degree of an Array

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.
'''

from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]):
        dict = {}
        for ind,val in enumerate(nums):
            if val not in dict:
                #列表中依次为 次数 , 最初索引, 最后索引, 长度差
                ini = ind
                dict[val] = [1,ini,0,1]
            else:
                now = ind
                dict[val][0] = dict[val][0]+1
                dict[val][2] = now
                dict[val][3] = now - dict[val][1]+1

        l = min([i for i in dict.values() if i[0] == max(dict.values(),key=lambda x:x[0])[0]],key=lambda x:x[3])[-1]
        return l 
     




s=Solution()
print(s.findShortestSubArray(nums = [1,2,2,3,1]))