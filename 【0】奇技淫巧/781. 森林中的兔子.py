# 森林中有未知数量的兔子。提问其中若干只兔子 "还有多少只兔子与你（指被提问的兔子）颜色相同?" ，
# 将答案收集到一个整数数组 answers 中，其中 answers[i] 是第 i 只兔子的回答。
#  给你数组 answers ，返回森林中兔子的最少数量。
# 示例 1：
# 输入：answers = [1,1,2]
# 输出：5
# 解释：
# 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
# 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
# 设回答了 "2" 的兔子为蓝色。
# 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
# 因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。
# 示例 2：
# 输入：answers = [10,10,10]
# 输出：11
#

import math
class mySolution:
    def numRabbits(self, answers):
        d = {}
        for  i in answers:
            d[i] = 0
        for i in answers:
            if i in d:
                d[i] +=1
        ans = 0
        for i in d:
            ans += math.ceil(d[i]/(i+1))*(i+1)
        return ans

from collections import Counter

class Solution:
    def numRabbits(self, answers) -> int:
        count = Counter(answers)
        ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        return ans

# 两只相同颜色的兔子看到的其他同色兔子数必然是相同的。
# 反之，若两只兔子看到的其他同色兔子数不同，那么这两只兔子颜色也不同。
#
# 因此，将 \textit{answers}answers 中值相同的元素分为一组，
# 对于每一组，计算出兔子的最少数量，然后将所有组的计算结果累加，就是最终的答案。
