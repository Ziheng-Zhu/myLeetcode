# 有四种面值的硬币：1，5，10，25，
# 现在需要给客户找零63元，最少需要给客户找零多少个硬币



# # i = 0
# def recMC(coinList,change):
#     # global i
#     # i+=1
#     minCoins = change
#     if change in coinList:
#         return 1
#     else:
#         list = [c for c in coinList if c<=change]
#         for i in list:
#             nums = 1 + recMC(coinList,change - i)
#             if nums < minCoins:
#                 minCoins = nums
#     return minCoins
#
#
# print(recMC([1,5,10,25],63))
# print(i)

def coinChange(coinList,change):
    def dp(n):
        #minchange = n
        if n==0:
            return 0
        if n<0:
            return -1
        res = float('INF')
        for coin in coinList:
            c = dp(n-coin)
            if c==-1:
                continue
            res = min(res,1+c)
        return res
    return dp(change)

#print(coinChange([1,5,10,11],63))


# 上面这个带有重复计算，下面通过备忘录来减少许多重复计算
def coinChange(coinList,change):
    memo = dict()
    def dp(n):
        #minchange = n
        if n in memo:
            return memo[n]
        if n==0:
            return 0
        if n<0:
            return -1
        res = float('INF')
        for coin in coinList:
            c = dp(n-coin)
            if c==-1:
                continue
            res = min(res,1+c)
        memo[n] = res
        return memo[n]
    return dp(change)

#print(coinChange([1,5,10,11],487))

# 数组迭代解法
def coinChange(coinList,change):
    dp = [change]*(change+1)
    dp[0] = 0
    #coinused = []
    for i in range(change+1):
        newcoin = 0
        for coin in coinList:
            if i<coin:
                continue
            else:
                #dp[i] = min(dp[i],1+dp[i-coin])
                if dp[i]>1+dp[i-coin]:
                     dp[i] = 1 + dp[i-coin]
         #            newcoin = coin
        #coinused.append(newcoin)
    return dp[change]

print(coinChange([1,5,10,11],65))

#想一下如何记录已经用的硬币