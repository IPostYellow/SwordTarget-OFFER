'''输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归方法 23ms 5752K
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:  # 若传进来的树为空，则深度为0，同时也是递归停止的条件
            return 0
        leftDeep = self.TreeDepth(pRoot.left)  # 递归左子树
        rigtDeep = self.TreeDepth(pRoot.right)  # 递归右子树
        if leftDeep > rigtDeep:
            return leftDeep + 1  # 若左子树高度更高，则用左子树高度加上当前这一层高度
        else:
            return rigtDeep + 1  # 若右子树高度更高，则用右子树高度加上当前这一层高度


# 遍历方法 46ms 5736K
class Solution2:
    def TreeDepth(self, pRoot):
        # 准备一个队列列表
        if pRoot==None:
            return 0
        deep = 0
        quelist = []
        quelist.append(pRoot)  # 根节点入队
        while (len(quelist) != 0):
            level_len = len(quelist)  # 存储当前层的列表长度
            for i in range(level_len):
                p = quelist.pop(0)  # 出队一个元素
                if p.left != None:  # 如果出队元素有左子树，则将左子树加入队列
                    quelist.append(p.left)
                if p.right != None:  # 如果出队元素有右子树，则将右子树加入队列
                    quelist.append(p.right)
            deep += 1  # 这一层遍历完毕
        return deep


# p = TreeNode(0)
# p.left = TreeNode(1)
# p.left.left = TreeNode(2)
# #
# T = Solution2()
# print(T.TreeDepth(p))
