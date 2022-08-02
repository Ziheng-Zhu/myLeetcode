# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    def plusOne(self, digits):
        digits[-1]+=1
        for i in range(len(digits)-2,-1,-1):
            if digits[i+1] == 10:
                digits[i+1] = 0
                digits[i] += 1
            else:
                break
        if digits[0] == 10:
            digits = [1] + digits
            digits[1] =0

        return digits


s = Solution()
print(s.plusOne([2,9,9,9]))