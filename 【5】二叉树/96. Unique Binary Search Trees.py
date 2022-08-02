# Given an integer n,
# return the number of structurally unique
# BST's (binary search trees) which has
#    'exactly n nodes of unique values from 1 to n.
#
class Solution:

    # 复杂度太高

    # def numTrees(self, n: int) -> int:
    #     def count(lo,hi):
    #         if lo>hi:
    #             return 1
    #         res = 0
    #         for i in range(lo,hi+1):
    #             left = count(lo,i-1)
    #             right = count(i+1,hi)
    #             res += left * right
    #         return res
    #     return count(1,n)

    # 利用备忘录
    def numTrees(self, n: int) -> int:
        memo = [ [0 for _ in range(n+1)] for _ in range(n+1)]
        # memo 不能写成 memo = [ [0]*(n+1)]]*(n+1)
        # 这种浅拷贝会将地址也拷贝进去
        def count(lo,hi):
            if lo>hi:
                return 1
            if memo[lo][hi] !=0:
                return memo[lo][hi]
            res = 0
            for i in range(lo,hi+1):
                left = count(lo,i-1)
                right = count(i+1,hi)
                res += left * right
            memo[lo][hi] = res
            return res

        return count(1,n)
