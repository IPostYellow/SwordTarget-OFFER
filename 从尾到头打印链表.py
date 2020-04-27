'''输入一个链表，按链表从尾到头的顺序返回一个ArrayList。'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 头插法
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        p = listNode
        array = []
        while (p != None):
            array.insert(0, p.val)
            p = p.next
        return array


A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A1.next = A2
A2.next = A3
P=Solution()
print(P.printListFromTailToHead(A1))
