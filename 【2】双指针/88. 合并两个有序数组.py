class Solution:
    def merge1(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

    # 双指针
    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1,p2 = 0,0
        while p1<m or p2<n:
            if p1==m:
                sorted.append(nums2(p2))
                p2 +=1
            elif p2==n:
                sorted.append(nums1[p1])
                p1 +=1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 +=1
            else:
                sorted.append(nums2[p2])
                p2 +=1
        nums1[:] = sorted

    #逆向双指针
    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2 = m-1,n-1
        tail = m+n-1
        while p1>=0 or p2>=0:
            if p1<0:
                nums1[tail] = nums2[p2]
                p2 -=1
            elif p2<0:
                nums1[tail]  = nums1[p1]
                p1 -=1
            elif nums1[p1]<= nums2[p2]:
                nums1[tail] = nums2[p2]
                p2 -=1
            else:
                nums1[tail] = nums1[p1]
                p1 -=1
            tail -=1