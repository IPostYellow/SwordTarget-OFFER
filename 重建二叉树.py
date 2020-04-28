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
