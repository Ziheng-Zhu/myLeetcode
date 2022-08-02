# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的
# 某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1],
#        nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，
# 如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。
#
class Solution:
    def search(self,nums,target):
        if not nums:
            return -1
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[l]:
                if nums[mid]>target>=nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid + 1
                else:
                    r = mid-1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            1. 二分查找的实现有两种方法，采用第一种：不断在循环体里面找到第一个错误的版本
            2. 抓住要点， 因为要使用二分查找法， 核心是，只有有序的区间内，才能判断出来是否有这个元素，
                这道题的关键点就变成了先判断有序区间，然后才能接着判断，元素在哪个区间，才能一步步缩小区间，然后求出结果！
            3. 观察下面步骤后其实就是一个递归的过程。 当落在有序区间了就是常规的二分查找。当落点还是无序的，那么等于又从头有序无序的判断一次， 一直缩小区间范围，对比target和 nums[mid]值
            4. 一定要注意细节！ 二分看似简单，全是细节。 错一个 =号，可能就会陷入死循环，或者程序走向错误的逻辑内！！！！
        """

        left, right = 0, len(nums) - 1

        # 感觉是一个递归过程
        while left <= right:
            # 1. 首先计算中间点mid
            mid = left + (right - left) // 2
            # 如果该点恰好等于 target，返回
            if nums[mid] == target: return mid
            # 3. 中点必将数组分为有序和无序上来那个部分，判断哪部分有序
            if nums[left] <= nums[mid]:
                # 注意这个等号不能少！ 测试用例[3, 1] 1 时。
                # nums[left] 和 nums[mid] 是有机会取相等的
                # 4. 前面有序，判断target在哪边
                if nums[left] <= target  and target < nums[mid]:
                    # target在有序这边
                    right = mid - 1
                else:
                    # 在无序这边
                    left = mid + 1
            else:
                # 5. 后面有序
                if nums[mid] < target and target <= nums[right]:
                    # target在有序这边
                    left = mid + 1
                else:
                    # 在无序这边
                    right = mid - 1

        # 6. 循环计数，未找到target，那么返回 -1
        return -1
