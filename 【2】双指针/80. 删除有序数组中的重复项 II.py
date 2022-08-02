# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
# 使每个元素 最多出现两次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组
# 并在使用 O(1) 额外空间的条件下完成。
#


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        slow, fast = 2, 2
        while fast < len(nums):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

