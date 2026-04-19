class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(num):
            l, r = 0, len(nums2)-1
            while l <= r:
                m = (l+r)//2
                if num <= nums2[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            return l-1
        
        maxDist = 0
        for i in range(len(nums1)):
            j = binarySearch(nums1[i])

            dist = 0 if (j - i) < 0 else j-i
                
            if dist > maxDist:
                maxDist = dist
        
        return maxDist