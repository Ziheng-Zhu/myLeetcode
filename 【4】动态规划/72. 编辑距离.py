# 给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0]* (n+1) for _ in range(m+1)]
        # 定义：dp[i][j] 返回 s1[0..i)和 s2[0..j) 的最小编辑距离
        for i in range(1,m+1):
            # 空字符串 到 长度为i的字符串的编辑距离为 i 步
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    # 二者在第 i 个字符相等，那么二者的前 i 位的编辑距离等于前 i-1 位
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 否则，就是 插入，删除，替换
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[m][n]