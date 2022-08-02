# Given an integer n, return an array ans of length n + 1 such
# that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.
#

class Solution:
    # 方法1
    def countBits(self, n: int):
        def bits(n):
            x = 0
            while n > 0:
                n = n & (n-1)
                x += 1
            return x
        return [bits(i) for i in range(n+1)]

    # 方法2
    def countBits2(self,n):
        bits = [0]
        hightBit = 0
        for i in range(1,n+1):
            if i & (i-1) == 0:
                hightBit = i
            bits.append(bits[i-hightBit]+1)
        return bits