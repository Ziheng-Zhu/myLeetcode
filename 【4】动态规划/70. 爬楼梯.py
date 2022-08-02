# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。

class Solution:
    #动态规划
    def climbStairs1(self, n: int) -> int:
        p = 1
        q = 2
        r = 3
        if n == 0:
            return 0
        if n == 1:
            return p
        if n == 2:
            return q
        if n == 3:
            return r
        for i in range(n-3):
            p = r
            r = r + q
            q = p
        return r

    #利用数组
    # 因为最后一步只有两种可能，
    # 要么是跨了一步，要么是垮了两步
    # 前者总共是f(n-1)，后者是f(n-2)
    # 两种可能数之和就是f(n)s
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return
        dp = [0,1,2]
        for i in range(3,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

s = Solution()
print(s.climbStairs(5))

