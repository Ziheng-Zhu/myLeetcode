# 给定一个非空整数数组，除了某个元素只出现一次以外，
# 其余每个元素均出现两次。
# 找出那个只出现了一次的元素。

from  functools import  reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return  reduce(lambda x,y: x^y, nums)