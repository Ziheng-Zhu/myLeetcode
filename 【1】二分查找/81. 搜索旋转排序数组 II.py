# 整数数组 nums 按非降序排列，数组中的值不必互不相同。
# 在传递给函数之前，nums 在预先未知的
# 某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1],
#        nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，
# 如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

class Solution:
    def search(self, nums, target: int) -> bool:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l +=1
                r -=1
            elif nums[mid] >= nums[l]:
                if  nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                if  nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid-1
        return False

sol = Solution()
print(sol.search([2,5,6,0,0,1,2],2))
print(sol.search([2,5,6,0,0,1,2],3))