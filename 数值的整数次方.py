# -*- coding:utf-8 -*-
class Solution:  # 20ms,5692k
    def Power(self, base, exponent):
        # write code here
        return pow(base, exponent)


# -*- coding:utf-8 -*-
class Solution2:#22ms,5720k
    def Power(self, base, exponent):
        # write code here
        if exponent > 0:
            tmp = base
            for i in range(exponent):
                base *= tmp
            return base
        elif exponent < 0:
            x = 1 / base
            tmp = x
            for i in range(-exponent):
                x *= tmp
            return x
        else:
            return 1


s = Solution2()
print(s.Power(2, 3))
