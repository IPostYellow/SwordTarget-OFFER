'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: #直接把遍历过的结点保存在列表里，然后判断新遍历的结点是否在列表里，如果是则直接返回这个在列表的结点。运行时间29ms，占用内存5860k
    history_list=[]
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # self.history_list.append(pHead)
        tmp=pHead
        while tmp.next!=None:
            self.history_list.append(tmp)
            tmp=tmp.next
            if tmp in self.history_list:
                return tmp
        return None

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
a.next=b
b.next=c
c.next=d

k=Solution()
z=k.EntryNodeOfLoop(a)
print(z)