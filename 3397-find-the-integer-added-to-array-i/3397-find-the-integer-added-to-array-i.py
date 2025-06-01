class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        n = len(nums1)

        if s1 < s2:
            return (s2 - s1) // n
        else:
            return (s2 - s1) // n