from collections import Counter

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = Counter(nums1)
        nums2Map = Counter(nums2) 

        first, second = 0, 0

        for num in nums1Map:
            if num in nums2Map:
                first += nums1Map[num]
        
        for num in nums2Map:
            if num in nums1Map:
                second += nums2Map[num]

        return [first, second]
        
        