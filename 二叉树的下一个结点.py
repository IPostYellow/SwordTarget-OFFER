'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:#运行时间22ms，占用内存5860k
    mid_list = []

    def midsearch(self, pNode):
        if pNode.left != None:
            self.midsearch(pNode.left)
        self.mid_list.append(pNode)
        if pNode.right != None:
            self.midsearch(pNode.right)

    def GetNext(self, pNode):
        # write code here
        tmp = pNode
        while tmp.next != None:
            tmp = tmp.next
        self.midsearch(tmp)
        if pNode == self.mid_list[-1]:#表示没有中序遍历下一个结点了
            return None
        for i in range(len(self.mid_list)-1):
            if pNode==self.mid_list[i]:
                return self.mid_list[i+1]


p=TreeLinkNode(1)
t=TreeLinkNode(2)
s=TreeLinkNode(3)
d=TreeLinkNode(4)

p.left=t
t.next=p
t.right=s
s.next=t
p.right=d
d.next=p

asd=Solution()
dddd=asd.GetNext(s)
print(dddd.val)