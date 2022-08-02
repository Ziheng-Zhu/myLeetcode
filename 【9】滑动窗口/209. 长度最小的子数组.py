# 给定一个含有n个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的
# 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        s = []
        minLen = 10E6
        for i in  nums:
            s.append(i)
            while sum(s) >= target:
                minLen = min(minLen,len(s))
                s.pop(0)
        if minLen <10E6:
            return minLen
        else:
            return 0