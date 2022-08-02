#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
# 同时保持非零元素的相对顺序。

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for fast in range(i+1,len(nums)):
        #             nums[fast-1],nums[fast] = nums[fast],nums[fast-1]
        #             print(i,nums)
        n = len(nums)
        left = right = 0
        while right<n:
            if nums[right] !=0:
                nums[left],nums[right] = nums[right], nums[left]
                left +=1
            right +=1


sol = Solution()
print(sol.moveZeroes([0,1,0,3,0,0,12]))

