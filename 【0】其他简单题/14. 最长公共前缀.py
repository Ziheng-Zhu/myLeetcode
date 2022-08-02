# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。

class Solution:
    def mylongestCommonPrefix(self, strs) -> str:
        if not strs:
            return "null"
        temp=""
        astr = strs[0]
        isEqual = True
        index = 0
        for ch in astr:
            for s in strs:
                if index>=len(s) or s[index]!=ch:
                    isEqual = False
                    break
            if not isEqual:
                break
            index = index+1
            temp = temp + ch
        return temp

    def longestCommonPrefix1(self,strs) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        count = len(strs)
        for i in range(1,count):
            prefix = self.lcp(prefix,strs[i])
            if not prefix:
                break
        return prefix


    def lcp(self,str1,str2):
        length = min(len(str1),len(str2))
        index = 0
        while index<length and str1[index] == str2[index]:
            index +=1
        return str1[:index]

    def longestCommonPrefix2(self,strs) -> str:
        if not strs:
            return ""

        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i==len(strs[j]) or strs[j][i] !=c for j in range(1,count)):
                return strs[0][:i]
        return strs[0]

#strs = ['flower','flow','flight']
#strs = ['ab','a']
#strs = []
strs = ['ab','a','abs','as']
s = Solution()
print(s.mylongestCommonPrefix(strs))
print(s.longestCommonPrefix1(strs))
print(s.longestCommonPrefix2(strs))