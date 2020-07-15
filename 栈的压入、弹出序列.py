'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


# -*- coding:utf-8 -*-
class Solution:#19ms,5752k
    def IsPopOrder(self, pushV, popV):
        # write code here
        for i in popV:
            if i not in pushV:
                return False
        stack_list = []
        p1 = 0
        p2 = 0
        while p1 < len(pushV) and p2 < len(popV):
            if pushV[p1] != popV[p2]:
                stack_list.append(pushV[p1])
                p1 += 1
            if pushV[p1] == popV[p2]:
                p1 += 1
                p2 += 1
                while (len(stack_list) > 0) and (popV[p2] == stack_list[-1]):
                    stack_list.pop(-1)
                    p2 += 1
        if p1 == len(pushV) and len(stack_list) == 0:
            return True
        else:
            return False

s=Solution()
print(s.IsPopOrder([1],[2]))