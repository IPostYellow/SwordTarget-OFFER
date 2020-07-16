'''
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 运行时间19ms,占用内存5624k
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val < pHead2.val:
            p1 = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            p1 = ListNode(pHead2.val)
            pHead2 = pHead2.next
        first = p1
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                p1.next = pHead1
                p1 = p1.next
                pHead1 = pHead1.next
            else:
                p1.next = pHead2
                p1 = p1.next
                pHead2 = pHead2.next

        p1.next = (pHead1 if pHead1 != None else pHead2)
        return first


class Solution2:#22ms,占用内存5688k
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


p = ListNode(1)
p2 = ListNode(2)
p.next = p2
p3 = ListNode(5)
p2.next = p3
p4 = ListNode(7)
p3.next = p4

q = ListNode(3)
q2 = ListNode(5)
q.next = q2
q3 = ListNode(6)
q2.next = q3
q4 = ListNode(8)
q3.next = q4

s = Solution2()
result = s.Merge(p, q)
print(result.val)
print(result.next.val)
print(result.next.next.val)
print(result.next.next.next.val)
print(result.next.next.next.next.val)
print(result.next.next.next.next.next.val)
print(result.next.next.next.next.next.next.val)
print(result.next.next.next.next.next.next.next.val)
