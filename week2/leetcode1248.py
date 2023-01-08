'''
1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k.
A continuous subarray is called nice if there are k odd numbers on it.
'''

from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # odd -> 1, even -> 0, k = sum of 1
        # then https://leetcode.com/problems/subarray-sum-equals-k/

        ps = defaultdict(int)

        count = 0
        sum = 0
        for num in nums:
            sum += num % 2  # num & 1 does the same
            if sum - k == 0:  # this can be replaced with ps[0] = 1 before the loop
                count += 1
            count += ps[sum - k]
            ps[sum] += 1

        return count
