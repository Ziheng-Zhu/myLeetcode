# 颠倒给定的 32 位无符号整数的二进制位。

class Solution:

    # 循环
    def reverseBits(self, n: int) -> int:
        res = 0
        for   i in range(32):
            res = (res <<1) | (n&1)
            n >>=1
        return res

    # 分治