# 给你一个m x n的矩阵mat和一个整数 k ，请你返回一个矩阵answer，
# 其中每个answer[i][j]是所有满足下述条件的元素mat[r][c] 的和：
#
# i - k <= r <= i + k,
# j - k <= c <= j + k 且
# (r, c)在矩阵内。

class Solution:
    def matrixBlockSum(self, mat, k: int):
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        # P[i][j]表示以mat 以(0,0)为左上段，(i-1,j-1)为右下端矩形子数组的元素之和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k,
                                                                                                            j - k)
        return ans
