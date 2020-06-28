'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''


# -*- coding:utf-8 -*-
class Solution:  # 22ms,占用内存5852k
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        q = numbers
        while len(q) > 0:
            s = q.pop(0)
            if s in q:
                duplication[0] = s
                return True

        return False


c = Solution()
x = [1]
print(c.duplicate([2, 3, 1, 0, 2, 5, 3], x))
print(x)


class Solution2: #21ms,5732k
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while i != numbers[i]:  # 只要这个索引下的值没有交换到等于这个索引的，就不断交换。
                if numbers[i] != numbers[numbers[i]]:
                    tmp = numbers[numbers[i]]
                    numbers[numbers[i]]=numbers[i]
                    numbers[i] = tmp
                else:
                    duplication[0] = numbers[i]
                    return True
        return False


c = Solution2()
x = [1]
print(c.duplicate([2, 3, 1, 0, 2, 5, 3], x))
print(x)