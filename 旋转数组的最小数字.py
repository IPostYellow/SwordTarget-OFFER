'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


# -*- coding:utf-8 -*-
class Solution:  # 482ms,5748k 在leetcode里执行时间为44ms，击败45.82%用户，内存消耗13.9MB击败9.23%
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        for i in range(len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]
        return rotateArray[0]


class Solution2:  # 513ms,5748k 在LeetCode里执行时间为32ms,击败96.9%用户，内存消耗13.8MB击败24.62%
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        left = 0
        right = len(rotateArray) - 1
        while left < right:
            print(left, right)
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            mid = left + (right - left) >> 1
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left += 1
        return rotateArray[left]


s = Solution2()
print(s.minNumberInRotateArray([1, 0, 1, 1, 1]))
