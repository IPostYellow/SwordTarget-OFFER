'''请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。'''
'''自己的思路'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        tmp = s.split(' ')
        str = "%20"
        return str.join(tmp)

'''进一步的思路,要修改原字符串'''
class Answer:
    def replaceSpace(self,s):
        return s.replace(" ","%20")

P=Answer()
print(P.replaceSpace("We Are Happy"))
