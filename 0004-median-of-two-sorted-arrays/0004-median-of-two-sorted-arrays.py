import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        nums1 = nums1+nums2
        nums1.sort()

        if (n1+n2) % 2 == 1:
            return float(nums1[(n1+n2)//2])
        else:
            upper_med = nums1[(n1+n2)//2]
            lower_med = nums1[(n1+n2)//2-1]
            return (upper_med+lower_med)/2
       

        