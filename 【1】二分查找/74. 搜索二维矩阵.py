# 编写一个高效的算法来判断m x n矩阵中，
# 是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = l+(r-l)//2
            rol = mid//n
            col = mid - rol*n
            if matrix[rol][col] == target:
                return True
            elif matrix[rol][col]>target:
                r = mid-1
            else:
                l = mid+1

        return False