#给定一个整数数组 nums ，找到一个具有最大和的连续子数组
# （子数组最少包含一个元素），返回其最大和。

class Solution:

    #动态规划
    def maxSubArray(self, nums) -> int:
        f = 0
        maxAns = nums[0]
        # f[i] 为 i 结尾的最大自序和
        for i in range(len(nums)):
            f = f + nums[i]
            f = max(f, nums[i])
            maxAns = max(maxAns,f)
        return maxAns

    #分治算法：


    #超出时间限制
    def maxSubArray1(self, nums) -> int:
        maxsubsum = nums[0]
        for head in range(len(nums)):
            for end in range(len(nums)-head+1):
                subset = nums[head:head+end]
                temp = sum(subset)
                if len(subset)>0 and maxsubsum < temp:
                    maxsubsum = temp
        return maxsubsum

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [5,4,-1,7,8]
#nums = [-2,-1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))


