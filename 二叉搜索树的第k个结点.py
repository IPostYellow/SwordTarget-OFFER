'''
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）中，按结点数值大小
顺序第三小结点的值为4。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 运行时间：34ms,占用内存5744k
    # 返回对应节点TreeNode
    def __init__(self):
        self.mid_list = []

    def midsearch(self, root):
        if root == None:
            return None
        else:
            if root.left:
                self.midsearch(root.left)
            self.mid_list.append(root)
            if root.right:
                self.midsearch(root.right)

    def KthNode(self, pRoot, k):
        # write code here
        if k < 1 or pRoot == None:
            return None
        self.midsearch(pRoot)
        if k > len(self.mid_list):
            return None
        else:
            return self.mid_list[k - 1]


class Solution2:  # 时间优化 运行时间：19ms,占用内存5624k
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
        self.mid_list = None

    def midsearch(self, root, k):
        if root == None:
            return None
        else:
            if root.left:
                self.midsearch(root.left, k)
            self.count += 1
            if self.count == k:
                self.mid_list = root
            if root.right:
                self.midsearch(root.right, k)

    def KthNode(self, pRoot, k):
        # write code here
        if k < 1 or pRoot == None:
            return None
        self.midsearch(pRoot, k)
        if self.mid_list == None:
            return None
        else:
            return self.mid_list


n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n5.left = n3
n5.right = n7
n3.left = n2
n3.right = n4
n7.left = n6
n7.right = n8

s = Solution()
print(s.KthNode(n5, 7).val)

#java 运行时间21ms,占用内存9716k
# import java.util.ArrayList;
#
# public class Solution {
#    ArrayList<TreeNode> list;
#     public Solution(){
#         list=new ArrayList();
#     }
#     public void inorder(TreeNode root){
#         if (root==null) return;
#         else{
#             if (root.left!=null) inorder(root.left);
#             list.add(root);
#             if (root.right!=null) inorder(root.right);
#         }
#     }
#     TreeNode KthNode(TreeNode pRoot, int k)
#     {
#         if (k<1) return null;
#         inorder(pRoot);
#         if (list.size()<k) return null;
#         return list.get(k-1);
#     }
# }
#
# class TreeNode {
#     int val = 0;
#     TreeNode left = null;
#     TreeNode right = null;
#     public TreeNode(int val) {
#         this.val = val;
#     }
# }

#运行时间：21ms,占用内存：9668k
# import java.util.ArrayList;
#
# public class Solution {
#    TreeNode result;
#     int count;
#     public Solution(){
#         result=null;
#         count=0;
#     }
#     public void inorder(TreeNode root,int k){
#         if (root==null) return;
#         else{
#             if (root.left!=null) inorder(root.left,k);
#             count++;
#             if (count==k){
#                 result=root;
#                 return;
#             }
#             if (root.right!=null) inorder(root.right,k);
#         }
#     }
#     TreeNode KthNode(TreeNode pRoot, int k)
#     {
#         if (k<1) return null;
#         inorder(pRoot,k);
#         if (result==null) return null;
#         return result;
#     }
# }
#
# class TreeNode {
#     int val = 0;
#     TreeNode left = null;
#     TreeNode right = null;
#     public TreeNode(int val) {
#         this.val = val;
#     }
# }