'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
'''


# -*- coding:utf-8 -*-
class Solution:  # 正常排序做 运行时间20ms 占用内存5732k
    number_list = []

    def Insert(self, num):
        # write code here
        self.number_list.append(num)

    def GetMedian(self, s):
        # write code here
        if len(self.number_list) == 1:
            return self.number_list[0]
        P = sorted(self.number_list)
        if len(P) % 2 == 0:
            return (P[len(P) // 2] + P[len(P) // 2 - 1]) / 2.0
        else:
            return P[len(P) // 2]


import heapq


class Solution2: #运行时间28ms，占用内存5720k

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def Insert(self, num):
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        print('max_heap1', self.max_heap)
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        # 上面的操作都是保证插入的元素到正确的位置中，如果正确位置在大顶堆的话，顺序就没错，然后返还一个大值给小堆。
        # 如果位置应该在小顶堆的话，那么肯定在大顶堆的堆顶，直接取出给小顶堆。
        # 就这样插入一个，给小堆一个。
        print('min_heap1', self.min_heap)
        if self.count & 1:  # 按位操作判断奇偶
            # 如果为奇数个元素，小顶堆比大顶堆少一个元素。所以要返还一个元素给大顶堆
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

        print('max_heap2', self.max_heap)
        print('min_heap2', self.min_heap)

    def GetMedian(self, s):
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2


# [5,2,3,4,1,6,7,0,8]
# S=Solution()
# S.Insert(5)
# print(S.GetMedian(1))
# S.Insert(2)
# print(S.GetMedian(1))
# S.Insert(3)
# print(S.GetMedian(1))
# S.Insert(4)
# print(S.GetMedian(1))
# S.Insert(1)
# print(S.GetMedian(1))
# S.Insert(6)
# print(S.GetMedian(1))
# S.Insert(7)
# print(S.GetMedian(1))
# S.Insert(0)
# print(S.GetMedian(1))
# S.Insert(8)
# print(S.GetMedian(1))

S = Solution2()
S.Insert(5)
print(S.GetMedian(1))
S.Insert(2)
print(S.GetMedian(1))
S.Insert(3)
print(S.GetMedian(1))
S.Insert(4)
print(S.GetMedian(1))
S.Insert(1)
print(S.GetMedian(1))
S.Insert(6)
print(S.GetMedian(1))
S.Insert(7)
print(S.GetMedian(1))
S.Insert(0)
print(S.GetMedian(1))
S.Insert(8)
print(S.GetMedian(1))
