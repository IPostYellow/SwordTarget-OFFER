'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 24ms,5876k
    def tree_hight(self, root):
        if root == None:
            return 0
        left_hight = self.tree_hight(root.left) + 1
        right_hight = self.tree_hight(root.right) + 1
        if left_hight > right_hight:
            return left_hight
        else:
            return right_hight

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True

        queue = [pRoot]
        while len(queue) > 0:
            tmp = queue.pop(0)
            if abs(self.tree_hight(tmp.left) - self.tree_hight(tmp.right)) > 1:
                return False
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return True


class Solution2:  # 后续遍历，可以先遍历左右子树，这样若果左右子树不满足，直接不需要判断根了。25ms,5636k
    def tree_hight(self, root):
        if root == None:
            return 0
        left_hight = self.tree_hight(root.left) + 1
        right_hight = self.tree_hight(root.right) + 1

        if left_hight > right_hight:
            return left_hight
        else:
            return right_hight

    def IsBalance(self, root):
        if abs(self.tree_hight(root.left) - self.tree_hight(root.right)) > 1:
            return False
        else:
            return True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if pRoot.left:
            if self.IsBalance(pRoot.left) == False:
                return False
            if self.IsBalanced_Solution(pRoot.left) == False:
                return False

        if pRoot.right:
            if self.IsBalance(pRoot.right) == False:
                return False
            if self.IsBalanced_Solution(pRoot.right) == False:
                return False

        if self.IsBalance(pRoot) == False:
            return False
        return True


x1 = TreeNode(1)
x2 = TreeNode(2)
x3 = TreeNode(3)
x4 = TreeNode(4)
x5 = TreeNode(5)
x6 = TreeNode(6)
x7 = TreeNode(7)
x1.left = x2
x1.right = x3
x2.left = x4
x2.right = x5

x3.right = x6
x5.left = x7

s = Solution2()
print(s.IsBalanced_Solution(x1))
