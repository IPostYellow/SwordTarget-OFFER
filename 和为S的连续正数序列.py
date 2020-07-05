'''
输出所有和为S的连续正数序列。
序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
import math

# -*- coding:utf-8 -*-
class Solution: #运行时间23ms 占用内存5752k
    def FindContinuousSequence(self, tsum):
        # write code here
        i = 1
        total_list = []
        while i < tsum:
            tmpsum = 0
            tmp = []
            j = i
            while tmpsum < tsum:
                tmpsum += j
                tmp.append(j)
                j += 1
                if tmpsum == tsum:
                    total_list.append(tmp)
            i = i + 1
        return total_list
#(x+y)*(y-x+1)
#y^2-x^2+x+y=200

class Solution2:#运行时间22ms,占用内存5624k
    def FindContinuousSequence(self, tsum):
        # write code here
        total_list=[]
        #y=-1+sqrt(1-4(-x^2+x-tsum))/2
        for x in range(1,tsum):
            y=(-1+math.sqrt(1-4*(-x*x+x-2*tsum)))/2
            if int(y)-y==0:
                total_list.append([i for i in range(x,int(y)+1)])
        return total_list

s = Solution2()
print(s.FindContinuousSequence(100))
