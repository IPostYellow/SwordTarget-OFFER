'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


# -*- coding:utf-8 -*-
class Solution:  # 运行时间18ms，占用内存5728k
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) < 1:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        mid = len(numbers) / 2
        num_dict = {}
        for i in numbers:
            if i in num_dict:
                num_dict[i] += 1
                if num_dict[i] > mid:
                    return i
            else:
                num_dict[i] = 1
        return 0


class Solution2:  # 候选法，运行时间18ms,占用内存5796k
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        cond = -1
        cnt = 0
        for i in range(len(numbers)):
            if cnt == 0:
                cond = numbers[i]
                cnt += 1
            else:
                if cond == numbers[i]:#相等就计数+1，否则就抵消掉
                    cnt += 1
                else:
                    cnt -= 1
        cnt=0
        for i in numbers:
            if i == cond:
                cnt+=1
        if cnt>len(numbers)/2:
            return cond
        else:
            return 0


s = Solution()
print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
