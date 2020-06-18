'''给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）'''
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        Alen = len(A)
        for i in range(Alen):
            tmp = 1
            for j in range(Alen):
                if j != i:
                    tmp *= A[j]
            B.append(tmp)
        return B


class Solution2:
    def multiply(self, A):
        B = [1]
        for i in range(1, len(A)):
            B.append(B[i - 1] * A[i - 1])
        tmp = 1
        for j in range(len(A) - 2, -1, -1):
            tmp *= A[j+1]
            B[j] *= tmp
        return B

p = Solution2()
e = p.multiply([1, 2, 3, 4, 5])
print(e)
