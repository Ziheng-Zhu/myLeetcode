# 给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        # dp[i][1] 表示第i天持有股票时积累的利润
        # dp[i][0] 表示第i天不持有股票时积累的利润
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]