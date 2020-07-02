'''
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，
即“XYZdefabc”。是不是很简单？OK，搞定它！
'''

# -*- coding:utf-8 -*-
class Solution:#运行时间32ms,占用内存5752k
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)<3:
            return ''
        tmp_list=list(s)
        while n>0:
            tmp=tmp_list.pop(0)
            tmp_list.append(tmp)
            n-=1
        return ''.join(tmp_list)

class Solution2:#运行时间22ms,占用内存5736k
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)<3:
            return ''
        tmp1=s[0:n]
        tmp2=s[n:]
        return tmp2+tmp1

s=Solution2()
print(s.LeftRotateString("abcXYZdef",3))