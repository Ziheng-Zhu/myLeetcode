# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，
# 同时仍保留空格和单词的初始顺序。
#
class Solution:
    # 双指针
    def reverseWords(self, s: str) -> str:
        s = list(s)
        slow = 0
        for pos in range(len(s)):
            if s[pos] ==" " or pos == len(s)-1:
                if s[pos] ==" ":
                    fast = pos-1
                if pos ==len(s)-1:
                    fast = pos
                while slow < fast:
                    s[slow], s[fast] = s[fast], s[slow]
                    slow += 1
                    fast -= 1
                slow = pos +1
        return ''.join(s)

    # 常规思路
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))

    def reverseWords(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]


s = "Let's take LeetCode contest"
sol = Solution()
print(sol.reverseWords(s))

## Input: s.split(' ')
## Output: ["Let's", 'take', 'LeetCode', 'contest']

## Input: word = 'take',word[::-1]
## Output: 'ekat'