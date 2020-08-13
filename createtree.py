class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]


def CreateTree(a):
    if len(a) == 0:
        return None
    treelist = []
    root = TreeNode(a[0])
    treelist.append(root)
    LevelNodeNum = 2
    StartIndex = 1
    RestNode = len(a) - 1

    while (RestNode > 0):
        i = StartIndex
        while i < (StartIndex + LevelNodeNum):
            CurNode = treelist.pop(0)
            if a[i] != None:
                CurNode.left = TreeNode(a[i])
                treelist.append(CurNode.left)
            if i + 1 == len(a):
                return root
            if a[i + 1] != None:
                CurNode.right = TreeNode(a[i + 1])
                treelist.append(CurNode.right)
            i += 2
        StartIndex += LevelNodeNum
        RestNode -= LevelNodeNum
        LevelNodeNum = len(treelist) * 2

    return root


def Inorder(root):
    if root == None:
        return None
    if root.left:
        Inorder(root.left)
    print(root.val)
    if root.right:
        Inorder(root.right)


TREE = CreateTree(a)
Inorder(TREE)

# java
# import java.io.*;
# import java.util.ArrayList;
# class test1
# {   public static TreeNode CreateTree(Integer[] nodelist){
#     if (nodelist.length==0) return new TreeNode(0);
#     ArrayList<TreeNode> TreeList=new ArrayList(0);
#     TreeNode root=new TreeNode(nodelist[0]);
#     TreeList.add(root);
#     int LevelNodeNum=2;
#     int StartIndex=1;
#     int RestNode=nodelist.length-1;
#
#     while (RestNode>0){
#         for(int i=StartIndex;i<(StartIndex + LevelNodeNum);i=i+2){
#             TreeNode CurNode=TreeList.remove(0);
#             if (nodelist[i]!=null){
#                 CurNode.left=new TreeNode(nodelist[i]);
#                 TreeList.add(CurNode.left);
#             }
#             if (i==nodelist.length-1) return root;
#             if (nodelist[i+1]!=null){
#                 CurNode.right=new TreeNode(nodelist[i+1]);
#                 TreeList.add(CurNode.right);
#             }
#         }
#         StartIndex=StartIndex+LevelNodeNum;
#         RestNode=RestNode-LevelNodeNum;
#         LevelNodeNum=TreeList.size()*2;
#     }
#     return root;
# }
#     public static void Inorder(TreeNode root){
#         if (root==null) return;
#         if (root.left!=null) Inorder(root.left);
#         System.out.println(root.val);
#         if (root.right!=null) Inorder(root.right);
#     }
#     public static void main (String[] args) throws java.lang.Exception
#     {
#         Integer[] nums = {5,4,8,11,null,13,4,7,2,null,null,null,1};
#         TreeNode root = CreateTree(nums);
#         Inorder(root);
#     }
# }
#
# class TreeNode
# {
#     int val=0;
#     TreeNode left=null;
#     TreeNode right=null;
#
#     public TreeNode(int x){
#         this.val=x;
#     }
# }
