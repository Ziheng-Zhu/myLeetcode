# #给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
# # 使每个元素 只出现一次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


class Solution:
    # 典型的双指针 Two Pointers
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow +=1
            fast +=1
        return slow

s = Solution()
print(s.removeDuplicates([1,1,2,3,3,4,4,4]))