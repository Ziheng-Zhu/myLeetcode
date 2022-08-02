# 给你一个非负整数数组nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#

class Solution:
    def jump(self, nums) -> int:
        """ 贪心策略解题 """
        """
            n 长度
            step 步长
            left, right 当前位置元素所能达到的第一个元素和最后一个元素
            cur 当前位置元素
        """
        n = len(nums)
        step =  0
        left, right, cur = 0,0,0

        if len(nums) == 1:
            return 0

        while left < n:
            # 更新当前元素的 left, right
            left = right + 1
            right = cur + nums[cur]

            if right >= n-1:
                return step + 1

            # 找到能走的最远的下一个元素
            temp = 0
            for i in range(left,right + 1):
                if i + nums[i] > temp:
                    temp = i + nums[i]
                    cur = i

            step += 1