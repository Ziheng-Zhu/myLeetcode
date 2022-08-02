# 给定一个数组，将数组中的元素向右移动k个位置，
# 其中k是非负数。
#
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        #nums  =nums[::-1]
        # 上面这个语句相当于指定了一个新的数组，名字也叫nums，在上面修改的是新的数组
        # 下面这个语句没有指定一个新的数组，在上面修改的时原数组
        nums[:]  =nums[::-1]
        print(nums)
        print(nums[k:])
        nums[k:] = nums[k:][::-1]
        nums[:k] = nums[:k][::-1]


s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums,3)
print(nums)