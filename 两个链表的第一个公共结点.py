# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 运行时间：18ms,占用内存：5764k
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        while p1 != None:
            p2 = pHead2
            while p2 != None:
                if p1 == p2:
                    return p1
                else:
                    p2 = p2.next
            p1 = p1.next
        return None


class Solution2:  # 运行时间：18ms,占用内存：5752k
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 != None:
                p1 = p1.next
            else:
                p1 = pHead2
            if p2 != None:
                p2 = p2.next
            else:
                p2 = pHead1
        return p1
