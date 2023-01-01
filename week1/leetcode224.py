'''
224. Basic Calculator


Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.
'''

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        # + / -  +:1 , -:-1
        oper = 1

        #sum
        res = 0

        #index
        i = 0

        while i<len(s):
            if s[i] ==' ':
                pass

            elif s[i].isdigit():
                value = s[i]
                while i+1<len(s) and s[i+1].isdigit():
                    i += 1
                    value += s[i]

                res += int(value) * oper

            elif s[i] =='+':
                oper = 1

            elif s[i] == '-':
                oper = -1

            elif s[i] =='(':
                stack.append(res)
                stack.append(oper)
                oper = 1
                res = 0

            elif s[i] ==')':
                formerSign = stack.pop()
                formerRes = stack.pop()
                res = formerRes + formerSign*res
            i+=1
        return res

a = Solution()
print(a.calculate("2147483647"))