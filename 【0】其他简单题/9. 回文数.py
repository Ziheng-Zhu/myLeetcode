#给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

#回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            s = str(x)
            l = len(s)
            index = 0
            # 注意while循环里index的取值范围
            while s[index]==s[-index-1] and index<l//2:
                index += 1
            if index == l//2:
                return True
            else:
                return False
        else:
            return False


    def isPalStr(self, aStr: str) -> bool:
        l = len(aStr)
        isEqual = True
        index = 0
        while aStr[index] == aStr[-index - 1] and isEqual and index < l // 2:
            index = index + 1
        if index == l // 2:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(0))
print(s.isPalindrome(1234))
print(s.isPalindrome(1234321))
#print(s.isPalStr('slss'))