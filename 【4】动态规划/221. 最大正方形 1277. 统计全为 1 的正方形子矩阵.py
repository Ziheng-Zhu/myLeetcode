# 在一个由 '0' 和 '1' 组成的二维矩阵内，
# 找到只包含 '1' 的最大正方形，并返回其面积。

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxSide = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2


#
#
# 1277. 统计全为 1 的正方形子矩阵
#
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp  = [[0]*n for _ in range(m)]
        #dp[i][j] 表示 以 (i,j) 为右下角的正方形子矩阵边长
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==1:
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                total += dp[i][j]
        return total



