# 给你一个按非递减顺排序的整数数组nums，返回
# 每个数字的平方组成的新数组，要求也按非递减顺序排序
#
#

class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        l,r,pos = 0,n-1,n-1
        ans  = [0]*n
        while l<=r:
            numl = nums[l]*nums[l]
            numr = nums[r]*nums[r]
            if numl >= numr:
                ans[pos] = numl
                l +=1
            else:
                ans[pos] = numr
                r -=1
            pos -=1
        return ans


