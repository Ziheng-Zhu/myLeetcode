# 给定一个整数数组，其中第i个元素代表了第i天的股票价格 。
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，
# 你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        # dp[i][1] 表示第i天持有股票时积累的利润
        # dp[i][0] 表示第i天不持有股票时积累的利润
        for i in range(n):
            if i==0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                continue
            if i==1:
                dp[1][0] = max(dp[0][0],dp[0][1]+prices[1])
                dp[1][1] = max(-prices[0], -prices[1])
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[n-1][0]