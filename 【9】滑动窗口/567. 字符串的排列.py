# 给你两个字符串s1和s2 ，
# 写一个函数来判断 s2 是否包含 s1的排列。
# 如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # counter1 为 s1 中每个字符出现的次数
        counter1 = collections.Counter(s1)
        N = len(s2)

        # 定义滑动窗口的范围为 [left,right] 闭区间
        left = 0
        right = len(s1)-1

        # 统计窗口 s2[left,right-1] 内的元素出现的次数
        counter2 = collections.Counter(s2[0:right])

        while right <N:
            # 把right 位置的元素放到 counter2中
            counter2[s2[right]] +=1
            # 如果滑动窗口中各个元素出现的次数和s1相等，
            # 则返回True
            if counter1 == counter2:
                return True
            # 窗口准备向东移动一格，left位置的元素出现次数就要减一
            counter2[s2[left]] -= 1

            # 如果当前位置出现次数为0，则需要从字典中把这个 key 删除掉
            # 否则会影响前面的if判断
            if counter2[s2[left]] ==0:
                del counter2[s2[left]]

            left +=1
            right +=1

        return False

