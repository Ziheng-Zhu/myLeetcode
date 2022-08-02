# 给你一个字符串 s，找到 s 中最长的回文子串。

class Solution:

    #  从中间拓展
    def longestPalindrome(self, s: str) -> str:
        def expandPalindrome(s,l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return l+1,r-1
        start,end = 0,0
        n = len(s)
        for i in range(n):
            l,r = expandPalindrome(s,i,i)
            if r-l > end-start:
                start,end= l,r
            l,r = expandPalindrome(s,i,i+1)
            if r-l > end-start:
                start,end= l,r
        return s[start: end+1]




    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0

        # dp[i][j] 表示 s[i..j] 是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 枚举字串长度
        for L in range(2, n + 1):
            # 枚举左边界
            for i in range(n):
                # 有边界：j-i+1 = L
                j = L - 1 + i
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][j] == true
                # 就表示s[i..j] 是回文字串
                # 此时需要记录回文长度以及起始位置
                if dp[i][j] and L > max_len:
                    max_len = L
                    begin = i
        return s[begin:begin + max_len]