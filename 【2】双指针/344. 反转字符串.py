# 编写一个函数，其作用是将输入的字符串反转过来。
# 输入字符串以字符数组 s 的形式给出。
#
# 不要给另外的数组分配额外的空间，
# 你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        slow = 0
        fast = l-1
        while slow < fast:
            s[slow],s[fast] = s[fast],s[slow]
            slow +=1
            fast -=1