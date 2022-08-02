# 给你两个整数数组nums1 和 nums2
# 请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，
# 应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
# 可以不考虑输出结果的顺序。

import collections

class Solution:

    # 使用哈希表

    def intersect(self, nums1,nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)

        d = collections.Counter()
        for num in nums1:
            d[num] +=1

        intersection = []

        for num in nums2:
            if d[num] >0:
                intersection.append(num)
                d[num] -=1
                # if d[num] ==0:
                #     d.pop(num)

        return intersection

    # 排序+ 双指针
