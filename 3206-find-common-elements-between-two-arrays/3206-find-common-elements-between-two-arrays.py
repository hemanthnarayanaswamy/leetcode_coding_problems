class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1U = set(nums1)
        nums2U = set(nums2) 

        first, second = 0, 0

        for num in nums1:
            if num in nums2U:
                first += 1
        
        for num in nums2:
            if num in nums1U:
                second += 1

        return [first, second]
        
        