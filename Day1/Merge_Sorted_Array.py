class Solution:
    def merge(self,nums1, m, nums2, n):
    # Start pointers at the end of nums1 and nums2
        p1 = m - 1
        p2 = n - 1
    # Start merging from the end of nums1
        current = m + n - 1
    
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[current] = nums1[p1]
                p1 -= 1
            else:
                nums1[current] = nums2[p2]
                p2 -= 1
            current -= 1
    
    # If there are remaining elements in nums2
        while p2 >= 0:
            nums1[current] = nums2[p2]
            p2 -= 1
            current -= 1
