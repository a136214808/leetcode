'''
2. Add Two Numbers

ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        result = root
        excess = 0

        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next

            result.next = ListNode(excess % 10)
            result = result.next
            excess = excess // 10

        return root.next