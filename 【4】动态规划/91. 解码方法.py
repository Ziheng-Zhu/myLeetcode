# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，
# 反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。
#

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1]+[0] * n
        for i in range(1,n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp = [1]+[0] * n
        # for i in range(1,n+1):
        #     if s[i-1] != '0':
        #         dp[i] = dp[i-1]
        #     if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
        #         dp[i] += dp[i-2]
        # return dp[-1]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c = b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                c += a
            a, b = b, c
        return c