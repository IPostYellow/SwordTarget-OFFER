'''请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。'''
'''自己的思路'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        tmp = s.split(' ')
        str = "%20"
        return str.join(tmp)

'''进一步的思路'''
class Answer:
    def replaceSpace(self,s):
        return s.replace(" ","%20")

'''用来面试时候的方法,指针方法'''
class Pointer:
    def replaceSpace(self, s):
        if str == "":
            return ""
        else:
            tmp = ""
            i = 0  # 遍历原字符串的指针
            # 由于python中string是不可变的。只能不停拼接
            while (i < len(s)):
                if s[i] == " ":
                    tmp += "%20"
                else:
                    tmp += s[i]
                i += 1
            return tmp

P=Answer()
print(P.replaceSpace("We Are Happy"))
