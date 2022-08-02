# 给定一个字符串，验证它是否是回文串，
# 只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。

class Solution:
    # 双指针
    def isPalindrome(self, s: str) -> bool:
        if not str:
            return True
        # 把s中字母和数字字符添加到s中
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        l = len(s)
        p1 = 0
        p2 = l-1
        while p1<p2:
            if s[p1]!=s[p2]:
                return False
            p1 +=1
            p2 -=1
        return True

    def isPalindrome(self, s: str) -> bool:
        # 把s中字母和数字字符添加到s中
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]

    # 在原字符串上直接用双指针
    def isPalindrome(self, s: str) -> bool:
        if not str:
            return True
        l = len(s)
        p1 = 0
        p2 = l-1
        while p1<p2:
            while p1<p2 and not s[p1].isalnum():
                p1 +=1
            while p1<p2 and not s[p2].isalnum():
                p2 -= 1
            if p1 <p2:
                if s[p1].lower() !=s[p2].lower():
                    return False
                p1 +=1
                p2 -=1
        return True