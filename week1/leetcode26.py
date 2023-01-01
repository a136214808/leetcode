'''
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''

        :param nums: list
        :return: length
        '''
        #get nums length
        n = len(nums)

        #index = 0
        res = 0

        #search
        for i in range(n):
            #two conditions that not duplicate:1.i==0 2.the former is not same as the latter
            if i==0 or nums[i] != nums[i-1]:
                nums[res] = nums[i]
                res +=1
        return res
