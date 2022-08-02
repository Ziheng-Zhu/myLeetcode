# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
#
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
#
# 假设每一种面额的硬币有无限个。
#
# 题目数据保证结果符合 32 位带符号整数。

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # N = len(coins)
        # dp = [[0]*(amount+1) for _ in range(N+1)]
        # # dp[i][j] 表示只使用前i个物品，当容量为j时，有dp[i][j] 种方法可以装满背包
        # for i in range(1,N+1):
        #     dp[i][0] = 1
        # for i in range(1,N+1):
        #     for j in range(1,amount+1):
        #         if coins[i-1] <= j:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # print(dp)
        # return dp[N][amount]
        N = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(N):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]