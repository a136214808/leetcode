'''
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1

        res = m+n-1

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[res] = nums1[i]
                i -=1
                res -=1
            else:
                nums1[res] = nums2[j]
                j -=1
                res -=1