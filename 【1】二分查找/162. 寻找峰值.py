# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组nums，找到峰值元素并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
#
class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)

        # 辅助函数
        def get(i):
            if i == -1 or i == n:
                return float('inf')
            return nums[i]

        l,r = 0,n-1
        while l<=r:
            mid = l+(r-l)//2
            if get(mid-1)<get(mid)>get(mid+1):
                return mid
            if get(mid) < get(mid+1):
                l = mid + 1
            else:
                r = mid-1
        return -1