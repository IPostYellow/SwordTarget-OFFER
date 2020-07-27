'''
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
'''

# -*- coding:utf-8 -*-
# 由于题目是使用32位的，所以比较蛋疼
class Solution:  # 运行时间19ms,占用内存5748k
    def NumberOf1(self, n):
        if n > 0:
            count = 0
            while n > 0:
                tmp = n % 2
                if tmp == 1:
                    count += 1
                n = n // 2
            return count
        elif n < 0 and n > -2147483648:
            n = -n
            bin_count = 0
            count = 0
            flag = 0  # 表示要不要开始计数，1表示开始,2表示带有进位
            while n > 0 or bin_count < 32:
                bin_count += 1
                tmp = 1 - n % 2  # 变成反码
                if tmp == 0 and flag == 0:  # 反码最后一位是0，所以补码直接+1没问题。
                    flag = 1
                    count += 1
                if tmp == 1 and flag == 0:  # 反码最后一位是1，所以补码直接+1后要进位
                    flag = 2
                if tmp == 1 and flag == 1:
                    count += 1
                if flag == 2 and tmp == 0:
                    flag = 1
                    count += 1
                if n > 0:
                    n = n // 2
            return count
        elif n <= -2147483648:
            return 1


class Solution2:  # 运行时间18ms,占用内存5748k
    def NumberOf1(self, n):
        ans = 0
        while n != 0 and n >= -2147483648:
            ans += 1
            n = n & (n - 1)
        return ans


s = Solution2()
print(s.NumberOf1(-8))
