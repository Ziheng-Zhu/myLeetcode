# Given two strings s and t, return true
# if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is
# formed from the original string by deleting
# some (can be none) of the characters without
# disturbing the relative positions of
# the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#


class Solution:

    # 双指针：
    def isSubsequence(self, s: str, t: str) -> bool:
        # l1 = len(s)
        # l2 = len(t)
        # p1 = 0
        # if not s:
        #     return True
        # for p2 in range(l2):
        #     if p1 >= l1:
        #         break
        #     if s[p1] == t[p2]:
        #         p1 +=1
        # if p1 == l1:
        #     return True
        # else:
        #     return False
        if s and not t:
            return False

        _s = _t = 0
        while _s < len(s) and _t < len(t):
            if s[_s] == t[_t]:
                _s += 1
            _t += 1
        return _s == len(s)

    # 动态规划：对于大量输入的 s 效果更好

