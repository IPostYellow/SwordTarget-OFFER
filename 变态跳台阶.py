#直接找规律 32 ms 5840K
class Solution:
    def jumpFloorII(self, number):
        # write code here
        result=1
        for i in range(number-1):
            result*=2
        return result
