'''
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words.
All the strings of words are of the same length.
'''
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]

        res = []
        sLen = len(s)
        wordNum = len(words)
        wLen = len(words[0])
        totalLen = wordNum*wLen

        dict = {}
        for i in words:
            dict[i] = dict.get(i,0)+1

        for i in range(0,sLen-totalLen+1):
            str = s[i:i+totalLen]
            dict2 = {}
            for j in range(0,len(str),wLen):
                if str[j:j+wLen] in dict:
                    dict2[str[j:j+wLen]] = dict2.get(str[j:j+wLen],0)+1

                if dict2 == dict:
                    res.append(i)
        return res


