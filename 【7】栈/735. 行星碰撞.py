# 给定一个整数数组 asteroids，表示在同一行的行星。
#
# 对于数组中的每一个元素，其绝对值表示行星的大小，
# 正负表示行星的移动方向（正表示向右移动，负表示向左移动）。
# 每一颗行星以相同的速度移动。
#
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
# 如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

class Solution:
    def asteroidCollision(self, asteroids):
        # 定义栈为留下来的行星
        ans = []
        for new in asteroids:
            # 只有当新的行星往左走，栈顶行星往右走，才会相撞
            while ans and new < 0 < ans[-1]:
                # 如果栈顶行星比新的行星小，则栈顶行星爆炸，
                # 新的行星保留，比较下一个栈顶的行星
                if ans[-1] < -new:
                    ans.pop()
                    continue
                # 如果栈顶行星和新的行星大小相同，则二者都爆炸
                elif ans[-1] == -new:
                    ans.pop()
                # 如果栈顶行星比新的行星大，或者相同，新的行星就爆炸了，
                # 所以就要退出循环，找下一个新的行星
                break
            # 不会相撞的行星则添加至栈顶
            else:
                ans.append(new)
        return ans

        # stack = []
        # flag =0
        # for i in asteroids:
        #     print(stack)
        #     while stack and stack[-1]>0 and i<0:
        #         if abs(i)>stack[-1]:
        #             stack.pop()
        #         elif abs(i) == stack[-1]:
        #             flag = 1
        #             stack.pop()
        #             break
        #         else:
        #             break
        #     if flag ==1:
        #         flag =0
        #         continue
        #     else:
        #         stack.append(i)
        # return stack

sol = Solution()
print(sol.asteroidCollision([10,2,-5]))