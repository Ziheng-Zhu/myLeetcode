# 给定两个字符串text1 和text2，
# 返回这两个字符串的最长 公共子序列 的长度。
# 如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的子序列是指这样一个新的字符串：
# 它是由原字符串在不改变字符的相对顺序的情况下
# 删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        # dp[i][j] 表示 text1[0:i-1], text2[0:j-1] 的最长公共子序列
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
