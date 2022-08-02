# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。


# [1,n] 中 k个数的组合，记答案为 s(1,n,k),
# s(1,n,k) = s(2,n,k) + {1}U s(2,n,k-1)
class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(temp,cur,n):
            # 如果temp大小是k个，那么就放进去
            if len(temp) == k:
                result.append(temp)
                return
            # 剪枝，如果当前temp太少了，
            # 少到即使把剩下的元素都加进去，都没有k个
            if len(temp) + n-cur+1 <k:
                return

            backtrack(temp,cur+1,n)
            # 这里不能用temp.append(cur)，因为这个方法不返回值
            backtrack(temp+[cur],cur+1,n)

        backtrack([],1,n)
        return result

sol = Solution()
print(sol.combine(4,2))