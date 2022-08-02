class Solution:
    Symbol_Value = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            #注意这里 i 的位置，如果i<n-1放在后面，就会出错！！！
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


    def myromanToInt(self, s: str) -> int:
        num = 0
        n = len(s)
        prev = Solution.Symbol_Value[s[0]]
        for i in range(n):
            v1 = prev
            if i< n-1:
                prev = Solution.Symbol_Value[s[i+1]]
            if i < n - 1 and v1 < prev :
                num = num - v1
            else:
                num = num + v1
        return num

s = Solution()
print(s.romanToInt('XIX'))
