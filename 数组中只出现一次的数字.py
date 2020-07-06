'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
'''


# -*- coding:utf-8 -*-
class Solution:  # 28ms,5644k
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        count = 0
        result = []
        while len(array) > 0:
            a = array.pop()  # 对元素进行出栈操作
            if a in array:
                array.remove(a)  # 若出栈的元素在列表里，说明这个数是出现了两次的，直接去掉。
            else:
                result.append(a)  # 否则就是答案
                count += 1
                if count == 2:
                    return result


# -*- coding:utf-8 -*-
class Solution2:  # remove操作比较费时间，所以可以换成用字典存储下出现的字，这样可以用空间换时间。21ms,5732k
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        count = 0
        result = []
        number_dict = {}
        while len(array) > 0:
            a = array.pop()  # 对元素进行出栈操作
            if a not in number_dict:
                number_dict[a] = 1
            if a in array:
                number_dict[a] += 1  # 若出栈的元素在列表里，说明这个数是出现了两次的，直接去掉。
            elif number_dict[a] == 1:
                result.append(a)  # 否则就是答案
                count += 1
                if count == 2:
                    return result
