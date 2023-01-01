'''
Move Zeroes

Given an integer array nums,
move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        n = len(nums)
        res = 0

        #move values that are not 0
        for i in range(n):
            if nums[i] !=0:
                nums[res] = nums[i]
                res +=1

        #append 0 to the end of the list
        while res<n:
            nums[res] = 0
            res +=1