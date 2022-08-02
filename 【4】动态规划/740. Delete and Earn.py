# You are given an integer array nums.
# You want to maximize the number of points you get
# by performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points.
# Afterwards, you must delete every element equal
# to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn
# by applying the above operation some number of times.
#

class Solution:
    # 转化成了 198. 打家劫舍
    def deleteAndEarn(self, nums) -> int:
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        a = total[0]
        b = max(total[0], total[1])
        for i in range(2, maxVal + 1):
            temp = b
            b = max(b, a + total[i])
            a = temp
        return b

    # 排序 + 动态规划
    # 更加节省空间和时间，将nums 分成连续的子数组
    def deleteAndEarn(self, nums) -> int:
        def rob(total):
            n = len(total)
            if n == 1:
                return total[0]
            a = total[0]
            b = max(total[0], total[1])
            for i in range(2, n):
                temp = b
                b = max(b, a + total[i])
                a = temp
            return b

        n = len(nums)
        ans = 0
        nums.sort()
        total = nums[0]
        for i in range(1,n):
            val = nums[i]
            if val == nums[i-1]:
                total[-1] += val
            elif val == nums[i-1] + 1:
                total.append(val)
            else:
                ans += rob(total)
                total = [val]
        ans += rob(total)
        return ans