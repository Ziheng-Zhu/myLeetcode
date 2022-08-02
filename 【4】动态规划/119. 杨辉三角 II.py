# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

class Solution:
    def getRow(self, rowIndex: int) :
        ans= [1]
        temp = ans
        for i in range(1,rowIndex+1):
            ans= [temp[j]+temp[j+1] for j in range(i-1) ]
            ans = [1] + ans+ [1]
            temp = ans
        return ans
