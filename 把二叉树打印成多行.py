'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 队列和计数器解决 运行时间30ms,占用内存5832k
    def Print(self, pRoot):
        # write code here
        if pRoot == {}:
            return []
        # 剑指offer上应该把代码改成这样
        # if pRoot==None:
        #   return []
        que_list = [pRoot]
        print_result = []
        count = 0
        tmp = []
        while len(que_list) > 0:
            if count == 0:
                count = len(que_list)
                tmp = []
            p = que_list.pop(0)
            tmp.append(p.val)
            count -= 1
            if count == 0:  # 代表当前层结束了
                print_result.append(tmp)
            if p.left != None:
                que_list.append(p.left)
            if p.right != None:
                que_list.append(p.right)
        return print_result


class Solution2:  # 带层次的bfs，运行时间22ms，占用内存5728k
    def Print(self, pRoot):
        if pRoot == {}:
            return []
        # if pRoot == None:
        #     return []
        ret = []
        queue = []
        queue.append(pRoot)

        while len(queue) > 0:
            sz = len(queue)
            ans = []
            while sz:
                tmp = queue.pop(0)
                ans.append(tmp.val)

                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                sz -= 1
            ret.append(ans)
        return ret


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(5)
p = Solution2()
print(p.Print(t))
