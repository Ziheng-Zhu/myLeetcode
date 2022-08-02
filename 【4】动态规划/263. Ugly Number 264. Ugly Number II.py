# An ugly number is a positive integer
# whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        factors = [2,3,5]
        for factor in factors:
            while n%factor ==0:
                n/=factor
        return True if n==1 else False
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        #  pi 表示得到更大的丑数需要乘 i 的 丑数 位置，i= 2,3,5
        #  dp[pi] 表示得到更大的丑数需要乘 i 的 丑数
        for i in range(2,n+1):
            num2,num3,num5 = dp[p2]*2,dp[p3]*3,dp[p5]*5
            dp[i] = min(num2,num3,num5)
            if dp[i] == num2:
                p2+=1
            if dp[i] == num3:
                p3+=1
            if dp[i] == num5:
                p5+=1
        return dp[-1]