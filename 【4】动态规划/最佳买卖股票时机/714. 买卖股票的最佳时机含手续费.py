# 给定一个整数数组prices，其中第i个元素代表了第i天的股票价格 ；
# 整数fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        # dp[i][1] 表示第i天持有股票时积累的利润
        # dp[i][0] 表示第i天不持有股票时积累的利润
        dp[0][0] = 0
        dp[0][1] = -prices[0]-fee
        for i in range(1,n):
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        return dp[n-1][0]
