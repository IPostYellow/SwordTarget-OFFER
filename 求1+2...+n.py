'''
求1+2+3+...+n，要求不能使用乘除法、
for、while、if、else、switch、case等关键字
及条件判断语句（A?B:C）。
'''
# -*- coding:utf-8 -*-
class Solution: #最简单的方法，递归加。然而这样耗时巨大 。运行时间31ms,占用内存5752k
    def Sum_Solution(self, n):
        # write code here
        return n+ ((n>0) and (self.Sum_Solution(n-1)))




s=Solution()
print(s.Sum_Solution(5))