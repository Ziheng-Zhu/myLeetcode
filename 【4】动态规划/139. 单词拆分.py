# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
# 请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，
# 并且字典中的单词可以重复使用。
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[n]