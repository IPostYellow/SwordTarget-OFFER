'''
统计一个数字在排序数组中出现的次数。
'''


# -*- coding:utf-8 -*-
class Solution:  # 21ms，5728k
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        for i in data:
            if i == k:
                count += 1
            if i > k:
                break
        return count


class Solution2:  # 二分搜索 17ms，5752k
    def GetNumberOfK(self, data, k):
        # write code here
        l = 0
        r = len(data)
        while (l < r):
            mid = (l + (r - 1)) // 2
            if data[mid] < k:  # 只会指向等于k的第一个值，如果没有等于k的值，则指向大于k的第一个值
                l = mid + 1
            else:
                r = mid

        l_bound = l
        l = 0
        r = len(data)
        while (l < r):
            mid = (l + (r - 1)) // 2
            if data[mid] <= k:  # 加个等号表示就算指向了等于k的还没结束，得指向大于k的第一个值
                l = mid + 1
            else:
                r = mid
        return l - l_bound  # 用第一个大于k的值的索引减去第一个等于k的值的索引即为答案，如果列表里不存在k，则两个第一个大于k的值的索引相减等于0


s = Solution2()
print(s.GetNumberOfK([5, 7, 7, 8, 8, 10], 8))
