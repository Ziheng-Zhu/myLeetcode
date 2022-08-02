# 给定一个已按照非递减顺序排列的整数数组numbers ，
# 请你从数组中找出两个数满足相加之和等于目标数target 。
#
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。
# numbers 的下标 从 1 开始计数 ，所以答案数组应当满足
# 1 <= answer[0] < answer[1] <= numbers.length 。
#
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

class Solution:
    # 双指针：
    def twoSum(self, numbers, target: int) :
        l, r = 0,len(numbers)-1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum>=target:
                r -=1
            else:
                l +=1
        return [-1,-1]

    # 二分查找
    def twoSum1(self, numbers, target: int) :
        n  = len(numbers)
        for i in range(n):
            l ,r = i+1,n-1
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == target-numbers[i]:
                    return[i+1,mid+1]
                elif numbers[mid]>target-numbers[i]:
                    r = mid-1
                else:
                    l = mid + 1
        return [-1,-1]
        # 为什么上一段可以，下一段却不可以
        # n = len(numbers)
        # for i in range(n):
        #     换个字母表示啊...target记录下来就递减了！！！
        #     target = target - numbers[i]
        #     l, r = i + 1, n - 1
        #     while l <= r:
        #         mid = l + (r - l) // 2
        #         if numbers[mid] == target:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return [-1, -1]


sol = Solution()
print(sol.twoSum1([5,25,75],100))