'''
811. Subdomain Visit Count

Given an array of count-paired domains cpdomains,
return an array of the count-paired domains of each subdomain in the input.
You may return the answer in any order.
'''
from typing import List

str = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

class Solution:
    def subdomainVisits(self, str):
        dict = {}

        for i in str:
            spl = i.split(' ')[1]
            v = int(i.split(' ')[0])
            n = len(spl)-1
            for j in range(n,-2,-1):
                if spl[j] == '.' or j==-1:
                    if spl[j+1:] not in dict:
                        dict[spl[j+1:]] = v
                    else:
                        dict[spl[j+1:]] +=v
        return [f'{values} {key}' for key,values in dict.items()]

a =Solution()
print(a.subdomainVisits(str))

