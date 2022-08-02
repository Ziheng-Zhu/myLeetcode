# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，
# 请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回  -1 。
#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if not needle:
                return 0
            elif not haystack:
                return -1
            l1 = len(haystack)
            l2 = len(needle)
            for i in range(l1-l2+1):
                if haystack[i] == needle[0] and haystack[i:i+l2] == needle:
                    return i
            return -1

s = Solution()
# haystack = "hello"
# needle = "ll"
haystack = 'aaaa'
needle = 'bba'
print(s.strStr(haystack,needle))
