# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为
# 非空
# 字符串且只包含数字
# 1
# 和
# 0。

# int(s,b),把b进制表示的字符串s，转化成十进制
# for example, s = '0110', b = 2, int(s,b) = 6

# bin(x), 把x转化为2进制

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
