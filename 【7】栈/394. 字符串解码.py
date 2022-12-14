# 394.字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的encoded_string正好重复k次。
# 注意k保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数k ，例如不会出现像3a或2[4]的输入。
#
# 示例1：输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例2：输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例3：输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"

class Solution:
    def decodeString(self, s: str) -> str:
        # 用stack来保存两个 [ 之间的字符
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                # 只要遇到 '[' 就把之前存储的数字和要重复的字符串入栈
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                # 只要遇到 ']' 就把栈顶的数字和字符串取出来
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                # 可能会遇到大于10的数字
                multi = 10 * multi + int(c)
            else:
                res += c
        return res