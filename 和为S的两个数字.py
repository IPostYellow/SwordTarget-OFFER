'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''


# -*- coding:utf-8 -*-
class Solution:  # 27ms 5752k
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) == 2:
            if array[0] + array[1] == tsum:
                return [array[0], array[1]]
            else:
                return []
        for i in range(len(array)):  # 从小开始遍历，第一个符合的肯定是乘积最小的。
            for j in range(i + 1, len(array)):
                if array[i] + array[j] > tsum:
                    break
                if array[i] + array[j] == tsum:
                    return [array[i], array[j]]
        return []


class Solution2:  # 哈希法，如果a+b=sum，则b=sum-a。运行时间22ms,占用内存5948k
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) == 2:
            if array[0] + array[1] == tsum:
                return [array[0], array[1]]
            else:
                return []
        tmp_mul = 999999999999
        tmp_list = ['a', 'a']
        array_dict = {}
        for i in range(len(array)):
            array_dict[array[i]] = i
        for i in range(len(array)):
            if (tsum - array[i]) in array_dict:
                tmp = (tsum - array[i]) * array[i]
                if tmp_mul > tmp:
                    tmp_mul = tmp
                    tmp_list[0] = array[i]
                    tmp_list[1] = tsum - array[i]

        if tmp_list[0] == 'a':
            return []
        else:
            return tmp_list


s = Solution2()
print(s.FindNumbersWithSum([1, 2, 5, 6, 9], 7))
