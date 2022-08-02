# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
#
# 你可以认为每种硬币的数量是无限的。

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount +1)
        dp[0] = 0
        #dp[i] 为金额 i 所需要用的最少的硬币
        # dp[0] = 0
        # dp[i] = min{ dp[i-coin] | coin in coins}
        for i in range(1,amount+1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]<amount+1 else -1