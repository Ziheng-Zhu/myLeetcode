# 给定一个整数数组，判断是否存在重复元素。
#
# 如果存在一值在数组中出现至少两次，函数返回
# true 。如果数组中每个元素都不相同，则返回
# false 。
#

class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = dict()
        for num in nums:
            if num in s:
                return True
            else:
                s[num]=0
        return False

    #   return len(list(set(nums))) < len(nums)