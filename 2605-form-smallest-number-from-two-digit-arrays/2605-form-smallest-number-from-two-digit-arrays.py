class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        commonNums = set(nums1) & set(nums2)

        if commonNums:
            return min(commonNums)

        n1 = min(nums1)
        n2 = min(nums2)

        return min(n1, n2) * 10 + max(n1, n2)