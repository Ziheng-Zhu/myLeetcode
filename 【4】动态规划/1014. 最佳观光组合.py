# 给你一个正整数数组 values，其中 values[i]表示第 i 个观光景点的评分，
# 并且两个景点i 和j之间的 距离 为j - i。
#
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，
# 也就是景点的评分之和 减去 它们两者之间的距离。
#
# 返回一对观光景点能取得的最高分。

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        mx = ans = 0
        for j in range(n):
            ans = max(ans,mx+values[j]-j)
            mx = max(mx,values[j]+j)
        return ans