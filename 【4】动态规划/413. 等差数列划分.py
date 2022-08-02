# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
#
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
#
# 子数组 是数组中的一个连续序列。
# 官方授权，非商业转载请注明出处。

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0

        dp = [0] * n
        # dp[i] 表示 dp[0],dp[1],..., dp[i] 中的等差数列的个数
        dp[0] = dp[1] = 0
        cut = nums[1] - nums[0]
        l = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == cut:
                l += 1
                dp[i] = dp[i - 1] + l
            else:
                dp[i] = dp[i - 1]
                cut = nums[i] - nums[i - 1]
                l = 0
        return dp[-1]