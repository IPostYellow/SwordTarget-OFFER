# -*- coding:utf-8 -*-
'''
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
'''
from createtree import CreateTree
from createtree import Inorder


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 21ms,5712k
    def __init__(self):
        self.istree = True
        self.find = False

    def findroot(self, pRoot1, pRoot2):
        if pRoot1 == None:
            return None
        if pRoot1.val == pRoot2.val:
            C = self.issame(pRoot1, pRoot2)
            if C:
                self.istree = True
                self.find = True
                return None
        if self.find == False:
            if pRoot1.left:
                self.findroot(pRoot1.left, pRoot2)
        if self.find == False:
            if pRoot1.right:
                self.findroot(pRoot1.right, pRoot2)

    def issame(self, proot1, proot2):
        T = True
        if proot1.val == proot2.val:
            if proot2.left:
                if proot1.left:
                    T = self.issame(proot1.left, proot2.left)
                    if T == False:
                        self.istree = False
                        return False
                else:
                    self.istree = False
                    return False
            if proot2.right:
                if proot1.right:
                    T = self.issame(proot1.right, proot2.right)
                    if T == False:
                        self.istree = False
                        return False
                else:
                    self.istree = False
                    return False
        else:
            self.istree = False
            return False
        return T

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1 == None:
            return False
        self.findroot(pRoot1, pRoot2)
        return self.istree


S = CreateTree([8, 8, 7, 9, 2, None, None, None, None, 4, 7])
S2 = CreateTree([8, 9, 2])
c = Solution()
print(c.HasSubtree(S, S2))

#java 10ms,9568k
#
# class TreeNode {
#     int val = 0;
#     TreeNode left = null;
#     TreeNode right = null;
#
#     public TreeNode(int val) {
#     this.val = val;
# }
# }
#
#
# public class Solution {
#     boolean istree=true;
#     boolean find=false;
#     public void findroot(TreeNode root1, TreeNode root2){
#     if (root1 == null) return;
#     if (root1.val == root2.val){
#     boolean C=issame(root1, root2);
#     if (C){
#     istree=true;
#     find=true;
#     return;
#     }
#     }
#     if (find == false){
#     if (root1.left != null) findroot(root1.left, root2);
#     }
#     if (find == false){
#     if (root1.right != null) findroot(root1.right, root2);
#     }
#     }
#     public boolean issame(TreeNode root1, TreeNode root2){
#     boolean T=true;
#     if (root1.val == root2.val){
#     if (root2.left != null){
#     if (root1.left != null){
#     T=issame(root1.left, root2.left);
#     if (T == false){
#     istree=false;
#     return false;
#     }
#     } else {
#         istree = false;
#     return false;
#     }
#     }
#     if (root2.right != null){
#     if (root1.right != null){
#     T = issame(root1.right, root2.right);
#     if (T == false){
#     istree=false;
#     return false;
#     }
#     } else {
#         istree = false;
#     return false;
#     }
#     }
#     } else {
#         istree = false;
#     return false;
#     }
#     return T;
#     }
# public boolean HasSubtree(TreeNode root1, TreeNode root2) {
#     if ((root1 == null) || (root2 == null)){
#         return false;
#     }
#     findroot(root1, root2);
#         return istree;
#     }
#     }