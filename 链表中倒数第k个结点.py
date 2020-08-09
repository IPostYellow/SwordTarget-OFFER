# -*- coding:utf-8 -*-
'''
输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 26ms,6520k 大小为k的滑动窗口
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return None
        count = 0
        p1 = head
        p2 = head
        while (count != k - 1):
            if p1.next != None:
                p1 = p1.next
                count += 1
            else:
                return None
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2


# class Solution2:  # 26ms,6520k 先将链表逆置，再取第k个元素。 不可用于剑指提交，因为剑指题目要求返回的是结点，不是值。如果以后遇到找倒数第k个值的可以用这个方法
#     def FindKthToTail(self, head, k):
#         # write code here
#         if head == None:
#             return None
#         p = head.next
#         p2 = ListNode(head.val)
#         while p != None:
#             tmp = p2
#             p2 = ListNode(p.val)
#             p2.next = tmp
#             p = p.next
#
#         count=0
#         while (p2!=None and count!=k-1):
#             count+=1
#             p2=p2.next
#         if count==k-1:
#             return p2
#         else:
#             return None

n1=ListNode(2)
n2=ListNode(3)
n3=ListNode(4)
n4=ListNode(5)
n1.next=n2
n2.next=n3
n3.next=n4
S=Solution()
print(S.FindKthToTail(n1,2).val)
# java 14ms,9576k
#
# class ListNode {
#     int val;
#     ListNode next = null;
#     ListNode(int val) {
#         this.val = val;
#     }
# }
# public class Solution {
#     ListNode p1;
#     ListNode p2;
#     int count;
#     public Solution(){
#         count=0;
#     }
#     public ListNode FindKthToTail(ListNode head,int k) {
#         if (head==null) return null;
#         p1=head;
#         p2=head;
#         while (count!=k-1){
#             if (p1.next!=null){
#                 p1=p1.next;
#                 count++;
#             }else return null;
#         }
#         while (p1.next!=null){
#             p1=p1.next;
#             p2=p2.next;
#         }
#         return p2;
#     }
# }