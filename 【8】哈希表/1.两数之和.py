#给定一个整数数组 nums和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


#暴力求解
# 时间复杂度:O(N^2)
# 空间复杂度:O(1)
def twosum1(nums,target):
    for i in range(len(nums)-1):
        base = nums[i]
        for j in range(i+1,len(nums)):
            if base + nums[j] == target:
                 return [i,j]


#哈希表：用一个哈希表存储试过的位置
# 时间复杂度: O(N)
# 空间复杂度: O(N)
def twosum2(nums,target):
    hashtable  = dict()
    for i,num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target-num],i]
        hashtable[nums[i]]=i
    return []


print(twosum1([2,7,11,15],9))

