# 请根据每日 气温 列表 temperatures ，
# 请计算在每一天需要等几天才会有更高的温度。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            # 如果栈不为空，且当前日期的气温大于栈顶日期的气温
            while stack and  temperatures[i] > temperatures[stack[-1]]:
                # 栈顶就出来
                prev_index = stack.pop()
                # 栈顶对应日期距离更高气温日期的天数= 当前日期-栈顶对应的日期
                ans[prev_index] = i - prev_index
            # 每次循环，都把当前日期添加进去栈顶
            stack.append(i)
        return ans
