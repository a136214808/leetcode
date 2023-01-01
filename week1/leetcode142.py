from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        #judge if  the link has cycle
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            #cycle exists
            if slow == fast:
                #find rukou
                a = slow
                b = head
                while a !=b:
                    a = a.next
                    b = b.next
                return a
        return None