# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#

class Solution:
    def generate(self, numRows: int):
        ans = [0 for i in range(numRows)]
        ans[0] = [1]
        for i in range(1,numRows):
            ans[i] = [ans[i-1][j]+ans[i-1][j+1] for j in range(i-1) ]
            ans[i] = [1] + ans[i] + [1]
        return ans