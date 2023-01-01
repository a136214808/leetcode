'''
Merge Two Sorted Lists

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pre = dummy

        while list1 and list2:
            if list1.val<=list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        if list1:
            pre.next = list1

        if list2:
            pre.next = list2

        return dummy.next

