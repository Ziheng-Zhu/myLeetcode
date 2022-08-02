# # 给定一个按照升序排列的整数数组 nums，和一个目标值 target。
# # 找出给定目标值在数组中的开始位置和结束位置。
# #
# # 如果数组中不存在目标值 target，返回[-1, -1]。
# #
# # 进阶：
# #
# # 你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
# #

class Solution:
    def searchRange(self,nums,target):
        def search_left(nums,target):
        # 返回 nums中出现 target的第一个位置
            n = len(nums)
            l,r = 0,n
            while l<r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    r = mid
                elif nums[mid]>target:
                    r = mid
                elif nums[mid]<target:
                    l = mid+1
            if l>= n or nums[l]!=target:
                return -1
            return l

        def search_right(nums,target):
        # 返回 nums中出现 target的最后一个位置
            n = len(nums)
            l,r = 0,n
            while l<r:
                mid = l+(r-l)//2
                if nums[mid] ==target:
                    l= mid+1
                elif nums[mid]>target:
                    r = mid
                elif nums[mid]<target:
                    l = mid+1
            if r==0:
                return - 1
            elif nums[r-1]!=target:
                return -1
            else:
                return r-1

        return [search_left(nums,target),search_right(nums,target)]


#
# class Solution:
#     def searchRange(self,nums,target):
#         # 寻找 target 在 nums 中最左边的位置
#         # 正是因为最坐标，所以只要是 nums[mid] >= target
#         # r 就必须要是 mid-1
#         # 循环终止条件是 l<=r ，所以循环跳出来的结果是就是l比r大1
#         # 此时的r是最左端位置-1，所以l满足要求
#         # 如果 target 不在 nums中，那么有三种情况
#         # target 比 nums 所有数字都大，那么 l 就等于 len(nums)
#         # 如果 target 比 nums 比所有数字都小，那么 l 就等于0，r=-1，
#         # 其余情况，就只需要验证 nums[l] == target 就可以了
#         def left_func(nums,target):
#             n = len(nums)-1
#             l,r = 0,n
#             while l<=r:
#                 mid = l+(r-l)//2
#                 if nums[mid]>= target:
#                     r = mid-1
#                 else:
#                     l=mid+1
#             return l
#         a = left_func(nums,target)
#         b = left_func(nums,target+1)
#
#         # 二分法可以用来判断
#         if a ==len(nums) or nums[a]!= target:
#             return [-1,-1]
#         else:
#             return [a,b-1]
# #nums = [5,7,7,8,8,10]
# nums = [1]
# sol = Solution()
# print(sol.searchRange(nums,1))