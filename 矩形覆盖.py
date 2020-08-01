'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法
'''


# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):#运行时间26ms，占用内存5684k
        # write code here
        if number <= 2:
            return number
        if number >= 3:
            n1=1
            n2=2
            result=0
            for i in range(3,number+1):
                result=n1+n2
                n1=n2
                n2=result
            return result


s = Solution()
print(s.rectCover(5))
