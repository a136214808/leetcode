
'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring
without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d,maxLen,start = {},0,-1
        for i in range(len(s)):
            if s[i] in d:
                prev = d[s[i]]
                start = max(prev,start)
            d[s[i]] = i
            maxLen = max(maxLen,i-start)
        return maxLen