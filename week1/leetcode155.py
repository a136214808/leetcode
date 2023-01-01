'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''

class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        pop = self.stack[-1]
        pop2 = self.min_stack[-1]
        if pop == pop2:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

