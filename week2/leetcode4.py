'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=[1,3]
        nums2=[2,4]
        nums3 = nums1 +nums2
        nums3  = sorted(nums3)
        if len(nums3)%2:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2-1]+nums3[len(nums3)//2])/2

