# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（
# 该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f = g = ans = nums[0]
        for i in range(1,n):
            ff, gg = f, g
            f = max( ff * nums[i], gg * nums[i] ,nums[i])
            g = min( gg * nums[i], ff * nums[i], nums[i])
            ans = max(ans,f)
        return ans