'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？
(子向量的长度至少是1)
'''


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):  # 18ms,5740k
        now_sum = []
        for i in range(len(array)):
            sum = array[i]
            now_sum.append(sum)
            for j in range(i + 1, len(array)):
                sum += array[j]
                now_sum.append(sum)
        return max(now_sum)


class Solution2:#动态规划法。结尾是第i个元素的序列中的最长连续子数组最大值为dp[i]，则dp[i]=max{dp[i-1]+array[i-1],array[i-1] 注意，第i个元素在array里索引是i-1}
    def FindGreatestSumOfSubArray(self, array):  # 18ms,5748k
        dp = []
        for i in range(len(array)+1):
            dp.append(0)
        ret = array[0]
        for i in range(1, len(array)+1):
            dp[i] = max(array[i - 1], (dp[i - 1] + array[i - 1]))
            ret = max(ret, dp[i])
        return ret


s = Solution2()
print(s.FindGreatestSumOfSubArray([2,8,1,5,9]))
