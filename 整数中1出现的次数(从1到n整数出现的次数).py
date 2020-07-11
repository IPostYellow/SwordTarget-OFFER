'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''


# # -*- coding:utf-8 -*-
# class Solution:#失败，数学方法好难
#     def NumberOf1Between1AndN_Solution(self, n):
#         # write code here
#         m = 10
#         sum = 0
#         while n >= m:
#             if n == m:
#                 return sum+2  # 加自己和最开始的1
#             sum += m
#             m *= 10
#         m = int(m / 10)
#         if n > 2 * m:
#             return sum + 1
#         else:
#             sum -= m
#             return sum + n - m + 2

class Solution:  # 运行时间37ms,占用内存5740k
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        for i in range(1, n + 1):
            tmp = i
            while tmp > 0:
                if tmp % 10 == 1:
                    sum += 1
                tmp = tmp // 10
        return sum


s = Solution()
print(s.NumberOf1Between1AndN_Solution(13))
