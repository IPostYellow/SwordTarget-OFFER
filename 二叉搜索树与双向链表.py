'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:#运行时间27ms,占用内存5752k
    def __init__(self):
        self.mid_order_list = []

    def mid_order(self, root_node):
        if root_node == None:
            return
        self.mid_order(root_node.left)
        self.mid_order_list.append(root_node)
        self.mid_order(root_node.right)
        # root_node.left = None
        # root_node.right = None

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        if pRootOfTree.left == None and pRootOfTree.right == None:
            return pRootOfTree
        self.mid_order(pRootOfTree)
        self.mid_order_list[0].left = None
        self.mid_order_list[0].right = self.mid_order_list[1]
        self.mid_order_list[-1].right = None
        self.mid_order_list[-1].left = self.mid_order_list[-2]
        for i in range(1, len(self.mid_order_list) - 1):
            self.mid_order_list[i].right = self.mid_order_list[i + 1]
            self.mid_order_list[i].left = self.mid_order_list[i - 1]

        # p = self.mid_order_list[0]
        # while p != None:
        #     print(p.val)
        #     p = p.right
        # print('-' * 80)
        # p = self.mid_order_list[-1]
        # while p != None:
        #     print(p.val)
        #     p = p.left
        return self.mid_order_list[0]


a1 = TreeNode(5)
a2 = TreeNode(4)
a3 = TreeNode(3)
a4 = TreeNode(2)
a5 = TreeNode(1)
a1.left = a2
a2.left = a3
a3.left = a4
a4.left = a5
s = Solution()
print(s.Convert(a1))
