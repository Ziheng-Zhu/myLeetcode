# 给定一个字符串s ,
# 请你找出其中不含有重复字符的最长子串的长度。
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        max_len = 0
        for ch in s:
            while ch in temp:
                temp = temp[1:]
            temp += ch
            if len(temp)>max_len:
                max_len = len(temp)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len +=1
            # 每次循环，判断当前的字符是否在队列中
            # 如果当前队列包含重复元素，就不满足要求
            # 此时需要移动这个队列；
            # 每次移动队列一次（删除一个重复元素），
            # 就要把当前队列长度减小1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -=1

            # 每次循环，去max_len为更大的队列长度
            if cur_len > max_len:
                max_len = cur_len

            # 每次循环加入s的一个字符
            lookup.add(s[i])
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用来记录每个字符是否出现过
        hash = set()
        n = len(s)
        # 右指针，初始值为-1，相当于在字符串的左边界左侧，还没有开始移动
        r, ans = -1,0
        for i in range(n):
            if i!= 0:
                # 左指针向右移动一格，移除一个字符
                hash.remove(s[i-1])
            while r + 1 < n and s[r+1] not in hash:
                # 不断移动右指针，直到右端的下一个字符没有出现
                hash.add(s[r+1])
                r += 1
            # 从第 i 个字符到第 r 个字符的字符串没有重复字符子串
            ans = max(ans,r-i+1)
        return ans

sol = Solution()
print(sol.lengthOfLongestSubstring('abcdabcefabc'))
