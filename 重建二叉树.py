'''输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre == []:
            return None
        tmpnode = TreeNode(0)
        sroot = pre[0]
        tmpnode.val = sroot
        left = tin.index(sroot)  # 刚好就是根节点左子树节点个数。
        right = len(tin) - left - 1  # 根节点右节点个数
        tmpnode.left = self.reConstructBinaryTree(pre[1:left + 1], tin[0:left])
        tmpnode.right = self.reConstructBinaryTree(pre[left + 1:], tin[left + 1:])
        return tmpnode
