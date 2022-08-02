# 给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。
# 你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        # dp[i][1] 表示第i天持有股票时积累的利润
        # dp[i][0] 表示第i天不持有股票时积累的利润
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[n-1][0]