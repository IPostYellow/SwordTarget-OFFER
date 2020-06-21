'''
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
'''
# -*- coding:utf-8 -*-
class Solution:  # 22ms,5856K
    def cheng(self, n):
        # 进了这个函数后，遍历的时候起码是切了两段以上。在分长度4以下的时候，直接返回那个数字
        # 因为长度4以下。再切分也不可能比自己大。直接返回自己，不要再分段了。
        # 比如f(5)=max{1*f(4),2*f(3),3*f(2),4*f(1)}。也就是分为两段，有以下情况(1,f(4)),(2,f(3),(3,f(2)),(4,f(1)))
        # 这种情况下，f(n<=4) 明显不再切分才比较大。
        '''
        最值型动态规划，比如求最大，最小值是多少
        计数型动态规划，比如换硬币，有多少种换法
        坐标型动态规划，比如在m*n矩阵求最值型，计数型，一般是二维矩阵
        区间型动态规划，比如在区间中求最值
        '''
        if n <= 4:
            return n

        tmp = 0
        for i in range(1, n):
            tmp = max(tmp, i * self.cheng(n - i))
        return tmp

    def cutRope(self, number):
        if number == 3:
            return 2
        if number == 2:
            return 1
        # write code here
        return self.cheng(number)


# 动态规划法，先存下f值
class Solution2: #33ms,6120k
    def cutRope(self, number):
        if number == 3:
            return 2
        if number == 2:
            return 1
        f = []
        for i in range(number + 1):
            f.append(0)
        for i in range(5):
            f[i] = i
        for j in range(5, number + 1):
            for k in range(1, j):
                f[j] = max(f[j], k * f[j - k])

        return f[number]


p = Solution2()
print(p.cutRope(5))
