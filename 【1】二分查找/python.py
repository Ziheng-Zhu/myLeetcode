nums1 = [1,4,7,8,10]
nums2 = [2,7,9,10,12]
sorted = []
m,n = len(nums1),len(nums2)
p1, p2 = 0, 0
while p1 < m or p2 < n:
    if p1 == m:
        sorted.append(nums2[p2])
        p2 += 1
    elif p2 == n:
        sorted.append(nums1[p1])
        p1 += 1
    elif nums1[p1] < nums2[p2]:
        sorted.append(nums1[p1])
        p1 += 1
    elif nums1[p1] > nums2[p2]:
        sorted.append(nums2[p2])
        p2 += 1
    elif nums1[p1]==nums2[p2]:
        sorted.append(nums1[p1])
        p1 +=1
        p2 +=1
print(sorted)