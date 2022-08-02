# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。
# 返回字符串中最后一个单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = len(s)
        flag = 0
        lastwordlen = 0
        for i in range(ls):
            last = s[ls-i-1]
            if last != ' ':
                lastwordlen +=1
                flag = 1
            if (last ==  ' '  or  i==ls-1 ) and flag ==1:
                return lastwordlen

s = "Hello World"
s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
s = 'abgdsgf'
sol = Solution()
print(sol.lengthOfLastWord(s))

