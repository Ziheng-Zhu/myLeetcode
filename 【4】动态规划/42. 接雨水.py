# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
# 计算按此排列的柱子，下雨之后能接多少雨水。

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l_max = [0]*n
        r_max = [0]*n
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            r_max[i] = max(r_max[i+1],height[i])

        for i in range(1,n-1):
            res += min(l_max[i],r_max[i])-height[i]
        return res