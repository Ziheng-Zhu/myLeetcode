# 编写一个函数，输入是一个无符号整数（以二进制串的形式），
# 返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for i in range(32) if n & (1<<i))

    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            # n & (n-1) 把 n 的二进制最后一个 1 变成 0
            n&=n-1
            ret+=1
        return ret