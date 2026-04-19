class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(idx, num):
            l, r = 0, len(nums2)-1
            while l <= r:
                m = (l+r)//2
                if num <= nums2[m]:
                    l = m + 1
                else:
                    r = m - 1

            if idx > l-1:
                return 0
            else:
                return l - 1 - idx
        
        maxDist = 0
        for i in range(len(nums1)):
            dist = binarySearch(i, nums1[i])
            print(dist, maxDist)
            if dist > maxDist:
                maxDist = dist
        
        return maxDist
