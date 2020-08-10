# -*- coding:utf-8 -*-
'''
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 20ms,5752k
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result = []
        self.tmp = []

    def preorder(self, root, sum):
        self.tmp.append(root.val)
        if (root.left == None) and (root.right == None) and (sum == root.val):
            self.result.append(copy.deepcopy(self.tmp))
        if root.left:
            self.preorder(root.left, sum - root.val)
        if root.right:
            self.preorder(root.right, sum - root.val)
        self.tmp.pop(-1) #开始回溯

    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        self.preorder(root, expectNumber)
        return self.result


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n6 = TreeNode(6)
n8 = TreeNode(8)
n5 = TreeNode(5)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n6
n2.right = n8
n3.left = n5
n3.right = n7
S = Solution()
print(S.FindPath(n1, 9))
#java 16ms,9796k
# import java.util.ArrayList;
# class TreeNode {
#     int val = 0;
#     TreeNode left = null;
#     TreeNode right = null;
#     public TreeNode(int val) {
#         this.val = val;
#     }
#
# }
# public class Solution {
#     ArrayList<ArrayList<Integer>> result;
#     ArrayList<Integer> tmp;
#     public Solution(){
#         result=new ArrayList<ArrayList<Integer>>();
#         tmp=new ArrayList<Integer>();
#     }
#     public void preorder(TreeNode root,int sum){
#         tmp.add(root.val);
#         if((root.left==null)&&(root.right==null)&&(root.val==sum)) result.add(new ArrayList<Integer>(tmp));
#         if(root.left!=null) preorder(root.left,sum-root.val);
#         if(root.right!=null) preorder(root.right,sum-root.val);
#         tmp.remove(tmp.size()-1);
#     }
#     public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
#         if (root==null) return result;
#         preorder(root,target);
#         return result;
#     }
# }
