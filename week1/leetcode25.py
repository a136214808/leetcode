'''
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        end = dummy

        #当end的每次遍历存在下一个对象
        while end.next != None:
            #判断是否在寻找过程中找到最后一位
            for i in range(k):
                if end == None:
                    break
                else:
                    end = end.next

            if end == None:
                break

            #为他们的下一位找个节点并断开联系
            start = pre.next
            pre.next = None

            ne = end.next
            end.next = None

            #开始翻转，并重新连接
            pre.next = self.reverse_list(start)
            start.next = ne

            #移动到下一次翻转位置
            pre = start
            end = start

        return dummy.next




    def reverse_list(self,head):
        if head == None or head.next == None:
            return head

        cur = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return cur