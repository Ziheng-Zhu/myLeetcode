# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
#
# 传送带上的第 i 个包裹的重量为 weights[i]。
# 每一天，我们都会按给出重量的顺序往传送带上装载包裹。
# 我们装载的重量不会超过船的最大运载重量。
#
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。



# 运载量最小值为包裹最大值，最大值为包裹重量和
# 在这样的区间里进行二分查找
# 如果D天能完成，那么说明最小天数小于等于D
# 如果D天不能完成运输，那么说明最小天数大于D
class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        l,r = max(weights),sum(weights)
        while l<r:
            mid = l+(r-l)//2
            need,total = 1,0
            for weight in weights:
                if total + weight >mid:
                    total = 0
                    need +=1
                total +=weight
            if need <= days:
                r = mid
            else:
                l = mid + 1
        return l




weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
sol = Solution()
print(sol.shipWithinDays(weights,D))