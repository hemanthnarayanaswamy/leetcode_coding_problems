import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_sorted = nums1+nums2
        merged_sorted.sort()
        n1, n2 = len(nums1), len(nums2)

        if (n1+n2) % 2 == 1:
            return float(merged_sorted[(n1+n2)//2])
        else:
            upper_med = merged_sorted[(n1+n2)//2]
            lower_med = merged_sorted[(n1+n2)//2-1]
            return (upper_med+lower_med)/2
       

        