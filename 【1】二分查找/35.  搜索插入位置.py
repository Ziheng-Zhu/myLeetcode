# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # left, right = 0, len(nums)
        # while left < right:
        #     mid = left + (right-left)//2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            print(l,r,mid)
            if nums[mid] ==target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid + 1
        return l

sol = Solution()
print(sol.searchInsert([1,3,5,6],2))

