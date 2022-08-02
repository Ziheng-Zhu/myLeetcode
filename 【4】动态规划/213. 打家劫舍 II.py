# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, mynums) -> int:
        if len(mynums) == 0:
            return 0

        if len(mynums) == 1:
            return mynums[0]

        if len(mynums) == 2:
            return max(mynums[0], mynums[1])

        def robRange(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        return max(robRange(mynums[0:-1]), robRange(mynums[1::]))