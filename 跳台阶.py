'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# -*- coding:utf-8 -*-
class Solution: #运行时间18ms,占用内存5744k
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        tmp = 0
        n1 = 1
        n2 = 2
        for i in range(3, number + 1):
            tmp = n1 + n2
            n1 = n2
            n2 = tmp
        return tmp

s=Solution()
print(s.jumpFloor(4))