'''
输入一个链表，反转链表后，输出新链表的表头。
'''


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 头插法 19ms,5624k
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        p=ListNode(pHead.val)
        pHead=pHead.next
        while pHead!=None:
            tmp=ListNode(pHead.val)
            tmp.next=p
            p=tmp
            pHead=pHead.next
        return p

a1=ListNode(1)
a2=ListNode(3)
a1.next=a2
a3=ListNode(5)
a2.next=a3
a4=ListNode(8)
a3.next=a4

s=Solution()
l=s.ReverseList(a1)
print(l.val)
print(l.next.val)
print(l.next.next.val)
print(l.next.next.next.val)