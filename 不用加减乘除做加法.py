class Solution:
    def Add(self, num1, num2):
        num1 = self.ten_to_two(num1)
        num2 = self.ten_to_two(num2)
        print(num1)
        print(num2)
        return self.two_to_ten(self.binary_add(num1, num2))

    def ten_to_two(self, num):
        binary = []
        result = num
        while result != 0:
            binary.append(result % 2)
            result = result // 2

        # binary.reverse()
        return binary  # 返回的是传入数字逆转后的二进制列表

    def two_to_ten(self, bianry_list):
        a = 1  # 二进制位数系数
        result = 0
        for i in bianry_list:
            result += i * a
            a *= 2
        return result

    def binary_add(self, num1, num2):
        '''
        :param num1:逆转后的二进制列表加数
        :param num2:逆转后的二进制列表被加数
        :return: 逆转后的二进制和
        '''
        while len(num1) > len(num2):  # 若num1长则将num2补长
            num2.append(0)
        while len(num2) > len(num1):  # 若num2长则将num1补长
            num1.append(0)
        num1.append(0)  # 防止最后一位进位
        num2.append(0)
        jinwei = 0
        p = 0  # 位数指针
        result = num1
        count = len(num1)  # 计算次数
        while count != p:
            print(result)
            if (num1[p] == 1) and (num2[p] == 1) and jinwei != 1:
                jinwei = 1
                result[p] = 0
            elif (((num1[p] == 1) and (num2[p] == 0)) or ((num1[p] == 0) and (num2[p] == 1))) and jinwei != 1:
                jinwei = 0
                result[p] = 1
            elif (num1[p] == 0) and (num2[p] == 0) and jinwei != 1:
                jinwei = 0
                result[p] = 0
            elif (num1[p] == 1) and (num2[p] == 1) and jinwei == 1:
                jinwei = 1
                result[p] = 1
            elif (((num1[p] == 1) and (num2[p] == 0)) or ((num1[p] == 0) and (num2[p] == 1))) and jinwei == 1:
                jinwei = 1
                result[p] = 0
            elif (num1[p] == 0) and (num2[p] == 0) and jinwei == 1:
                jinwei = 0
                result[p] = 1
            p += 1

        return result


# 设a，b位两个二进制数，则a+b=a^b+(a&b)<<1
class Solution2:
    '''
    当异号数相加大于0时，进位为负数，带符号左移时不断变小，因此统一转换为加数相反数之和，取反
    '''

    def Add(self, a, b):  # 非递归
        if a == 0:
            return b
        if b == 0:
            return a
        if self.add(~a, 1) == b:  # self.add(~a,1)其实就是起到了-a的作用
            return 0
        if a > 0 and b < 0:
            temp = self.add(~b, 1)
            if temp > a:
                return self.add(a, b)  # 如果是小减大，则直接加就好了
            if temp < a:
                temp_result = self.add(temp, self.add(~a,
                                                      1))  # 如果是大减小，比较麻烦，因为异号数相加大于0的时候，进位为负，然后随着左移操作，会越来越小（绝对值越来越大），根本不可能到0，所以必须则反过来操作，再把最后结果取反
                return self.add(~temp_result, 1)
        elif a < 0 and b > 0:
            temp = self.add(~a, 1)
            if temp > b:
                return self.add(b, a)
            if temp < b:
                temp_result = self.add(temp, self.add(~b, 1))
                return self.add(~temp_result, 1)
        elif a < 0 and b < 0:
            temp_result = self.add(self.add(~a, 1), self.add(~b, 1))
            return self.add(~temp_result, 1)
        else:
            return self.add(a, b)

    def add(self, a, b):
        while b:
            sum = a ^ b  # 异或得到两数之和
            carry = (a & b) << 1  # 取得进位
            a = sum
            b = carry
        return a


# 第一个方法超了内存限制
p = Solution2()
print(p.Add(-1, 8))
