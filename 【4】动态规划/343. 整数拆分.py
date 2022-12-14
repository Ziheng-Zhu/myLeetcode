#给定一个正整数 n，将其拆分为至少两个正整数的和，
# 并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2,n+1):
            for j in range(i):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
                # 对于dp[i]，包含j的因子，i-j要么分解，要么不分解
        return dp[n]
