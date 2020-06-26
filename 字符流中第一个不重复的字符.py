'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字
符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一
次的字符是"l"。
'''


# -*- coding:utf-8 -*-
class Solution:#运行时间21ms，占用内存5732k
    # 返回对应char]
    def __init__(self):
        self.no_one_dict = {}
        self.one_list=[]
    def FirstAppearingOnce(self):
        # write code here
        for i in self.one_list:
            if self.no_one_dict[i]==1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        if self.no_one_dict.get(char) != None:
            self.no_one_dict[char] +=1
        elif self.no_one_dict.get(char)==None:
            self.no_one_dict[char]=1
            self.one_list.append(char)

        return self.FirstAppearingOnce()



p = Solution()
print(p.Insert('h'))
print(p.Insert('e'))
print(p.Insert('l'))
print(p.Insert('l'))
print(p.Insert('o'))
print(p.Insert('w'))
print(p.Insert('r'))
print(p.Insert('o'))
print(p.Insert('l'))
print(p.Insert('d'))
