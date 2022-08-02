# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#
# 官方授权，非商业转载请注明出处。

class Solution:
    # def canJump(self, nums) -> bool:
    #     n = len(nums)
    #     # dp 表示当前位置 所能达到的最远点
    #     # 是 前一步到达最远点-1 和 当前数组值的最大值
    #     dp = [0] * n
    #     dp[0] = nums[0]
    #     for i in range(1,n):
    #         if dp[i-1] == 0:
    #             return False
    #         dp[i] = max(dp[i-1]-1,nums[i])
    #     return True
    def canJump(self, nums) -> bool:
        n = len(nums)
        a = nums[0]
        for i in range(1,n):
            if a == 0:
                return False
            temp = a
            a = max(a-1,nums[i])
        return True