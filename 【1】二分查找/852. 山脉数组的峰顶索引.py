# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i< arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足
# arr[0] < arr[1] < ... arr[i - 1] < arr[i] >
# arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        l, r = 1,len(arr)-2
        while l<=r:
            mid = l+(r-l)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid-1]:
                r = mid-1
            elif arr[mid]<arr[mid+1]:
                l = mid + 1
