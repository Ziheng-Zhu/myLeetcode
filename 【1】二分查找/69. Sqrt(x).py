# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

class Solution:
    def mySqrt1(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(x+1):
            if i*i>x:
                return i-1
            if i*i == x:
                return i

# 二分查找
    def mySqrt(self, x: int) -> int:
        # ans 用来记录 答案，当l=r时，退出循环了
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l+r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


