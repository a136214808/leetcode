'''
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
'''
from typing import List

import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        cal = lambda x,oper,y:eval(str(y)+oper+str(x))
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                left = stack.pop()
                right = stack.pop()
                result = cal(left,i,right)
                if i=='/':
                    result = math.ceil(result) if result < 0 else math.floor(result)
                stack.append(result)
        return int(stack.pop())


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

a = Solution()
print(a.evalRPN(tokens))
