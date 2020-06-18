'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
#直接找规律 32 ms 5840K
class Solution:
    def jumpFloorII(self, number):
        # write code here
        result=1
        for i in range(number-1):
            result*=2
        return result

#运行时间26ms 5860K
class Solution2:
    def jumpFloorII(self, number):
        f=[]
        f.append(1)#f[0]=1
        f.append(1)#f[1]=1
        for i in range(number-1):
            tmp_sum=0
            for j in f:
                tmp_sum+=j
            f.append(tmp_sum)
        return f.pop()


p=Solution2()
a=p.jumpFloorII(0)
print(a)