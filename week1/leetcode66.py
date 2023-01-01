
'''
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] !=9:
                digits[i]+=1
                for j in range(i+1,n):
                    digits[j] = 0
                return digits
        return [1]+[0] *n



