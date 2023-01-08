'''
1. Two Sum

Given an array of integers nums
and an integer target,
return indices of the two numbers such that they add up to
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for ind,val in enumerate(nums):
            if target-val not in map:
                map[val] = ind
            else:
                return [map[target-val],ind]