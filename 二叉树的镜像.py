class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 直接思路，不断递归交换左右子树 运行时间22ms 占用内存5876k
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        # 交换左右子树
        if root == None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        if root.left != None:
            self.Mirror(root.left)
        if root.right != None:
            self.Mirror(root.right)
        return root


# 非递归方法 运行时间21ms 占用内存5736K
class Solution2:
    def Mirror(self, root):
        if root == None:
            return root
        stack_list = [root]
        while len(stack_list)>0:
            p=stack_list.pop()
            tmp = p.left
            p.left = p.right
            p.right = tmp
            if p.left != None:
                stack_list.append(p.left)
            if p.right != None:
                stack_list.append(p.right)

        return root

tree1 = TreeNode(8)
tree2 = TreeNode(6)
tree3 = TreeNode(10)
tree4 = TreeNode(5)
tree5 = TreeNode(7)
tree6 = TreeNode(9)
tree7 = TreeNode(11)
tree2.left = tree4
tree2.right = tree5
tree3.left = tree6
tree3.right = tree7
tree1.left = tree2
tree1.right = tree3

p = Solution2()
root = p.Mirror(tree1)
print(1)
