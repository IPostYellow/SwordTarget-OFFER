'''
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
'''
# -*- coding:utf-8 -*-
class Solution:#超时
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            return n
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

class Solution2: #16ms,5744k
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            return n
        if n==2:
            return 1
        n1=1
        n2=1
        tmp=0
        for i in range(3,n+1):
            tmp=n1+n2
            n1=n2
            n2=tmp
        return tmp

s=Solution2()
print(s.Fibonacci(6))
s=Solution()
print(s.Fibonacci(6))