'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

# -*- coding:utf-8 -*-
class Solution:# 17ms,5744k
    def jugleBST(self,sequence,l,r):
        if l>=r:
            return True
        root = sequence[r]
        mid = l
        for i in range(l, r+1):#如果没有到r+1,会漏掉全是左子树的情况
            mid = i
            if sequence[i] > root:
                break
        for j in range(mid, r):
            if sequence[j] < root:
                return False
        if mid-l<=1:
            left=True
        else:
            left=self.jugleBST(sequence, l, mid - 1)
        if r-mid<=1:
            right=True
        else:
            right=self.jugleBST(sequence, mid, r-1)
        # return self.jugleBST(sequence, l, mid - 1) and self.jugleBST(sequence, mid, r - 1)
        return left and right
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.jugleBST(sequence, 0, len(sequence)-1)

s=Solution()
print(s.VerifySquenceOfBST([4,6,7,5]))

