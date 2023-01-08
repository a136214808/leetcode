'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs=["eat","tea","tan","ate","nat","bat"]

        mp = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch)-ord('a')]+=1
            mp[tuple(counts)].append(st)
        return mp.values()