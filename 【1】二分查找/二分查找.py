# 在排好序的数组中查找给定的数
def binarysearch(arr,k):
    l, r = 0,len(arr)-1
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] == k:
            return mid
        elif arr[mid]>k:
            r = mid-1
        else:
            l = mid+1
    return -1

# 在排好序的数组中，查找最接近给定数字的数
def binaryapprox(arr,k):
    l,r = 0,len(arr)-1
    while l<r:
        mid = l + (r-l)//2
        if arr[mid]<k:
            l = mid +1
        else:
            r = mid
    return l



print(binarysearch([1,2,3,4,5,6,7],3))
print(binaryapprox([1,2,3,4,5,6,7],3.6))