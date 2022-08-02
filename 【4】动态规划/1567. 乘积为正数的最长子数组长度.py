# 给你一个整数数组 nums，请你求出乘积为正数的最长子数组的长度。
#
# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
#
# 请你返回乘积为正数的最长子数组长度。
#

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos = int(nums[0]>0)
        neg = int(nums[0]<0)
        maxLen = pos
        for i in range(1,n):
            if nums[i] > 0:
                pos += 1
                neg = (neg + 1 if neg>0 else 0 )

            elif nums[i] < 0:
                # 两个变量在前后迭代中互相干扰，所以要新定义两个变量
                newneg = pos + 1
                newpos = (neg+1 if neg>0 else 0)
                pos,neg = newpos,newneg
            else:
                pos = neg = 0
            maxLen = max(maxLen, pos)
        return maxLen

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # pos[i]: 以下标i结尾乘积>0的最长子数组长度
        # neg[i]: 以下标i结尾乘积<0的最长子数组长度
        pos = [0] * n
        neg = [0] * n
        maxLen = 0
        for i in range(n):
            if i ==0:
                if nums[0]>0:
                    pos[i] = 1
                elif nums[0]<0:
                    neg[i] = 1
            else:
                if nums[i] > 0:
                    pos[i] = pos[i-1] + 1
                    if neg[i-1] > 0:
                        neg[i]=neg[i-1]+1
                    else:
                        neg[i] = 0
                elif nums[i]<0:
                    neg[i] = pos[i-1] + 1
                    if neg[i-1] > 0:
                        pos[i] = neg[i-1] + 1
                    else:
                        pos[i] = 0
                else:
                    pos[i] = neg[i] = 0
            maxLen = max(maxLen,pos[i])
        return maxLen
