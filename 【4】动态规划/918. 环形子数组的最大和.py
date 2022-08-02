# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
#
# 在此处，环形数组意味着数组的末端将会与开头相连呈环状。
# （形式上，当0 <= i < A.length 时 C[i] = A[i]，
# 且当 i >= 0 时 C[i+A.length] = C[i]）
#
# 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。
# （形式上，对于子数组 C[i], C[i+1], ..., C[j]，
# 不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        # 环形数组求和有两种情况
        # 一：连续，可以用 53 来解决
        # 二：前缀加后缀，等于数组和减去最小子数组和，
        # 但是要注意子数组的存在性，
        # 如果最小子数组和 等于 整个数组的和，那么这个最小子数组就不存在
        #

        f = minSum  = nums[0]
        g = maxSum = nums[0]
        for i in range(1,len(nums)):
            f = min(f+ nums[i],nums[i])
            minSum = min(minSum, f)
            g = max(g+nums[i],nums[i])
            maxSum = max(maxSum,g)

        return max(maxSum,sum(nums)-minSum) if minSum < sum(nums) else maxSum


        # 超出时间限制
        # def maxSubarraySum(mynums):
        #     f = maxAns = mynums[0]
        #     for i in range(1, n):
        #         print(i)
        #         f = max(f + mynums[i], mynums[i])
        #         maxAns = max(maxAns, f)
        #     return maxAns
        #
        # maxAns = -float('inf')
        # n = len(nums)
        # for i in range(n):
        #     if i >= 1:
        #         mynums = mynums + [mynums.pop(0)]
        #     else:
        #         mynums = nums
        #     print(mynums)
        #     maxAns = max(maxAns, maxSubarraySum(mynums))
        # return maxAns