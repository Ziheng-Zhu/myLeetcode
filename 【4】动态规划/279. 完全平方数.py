# 给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）
# 使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；
# 换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j=1
            minn = float('inf')
            while j*j<=i:
                minn = min(minn,dp[i-j*j])
                j+=1
            dp[i] = minn + 1
        return dp[n]