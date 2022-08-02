# 给你一个字符串数组 words ，
# 请你找出所有在 words 的每个字符串中都出现的共用字符
# （ 包括重复字符），并以数组形式返回。
# 你可以按 任意顺序 返回答案。

class Solution:
    def commonChars(self, words):
        res = []
        min_len_str = min(words,key = len)
        for ch in min_len_str:
            if all(ch in item for  item in words):
                res.append(ch)
                words = [i.replace(ch,'',1) for i in words]
        return res



words = ["cool","lock","cook"]
sol = Solution()
print(sol.commonChars(words))
