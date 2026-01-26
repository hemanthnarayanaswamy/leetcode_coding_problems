class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        commonNums = set(nums1) & set(nums2)

        if commonNums:
            return min(commonNums)

        min1 = min(nums1)
        min2 = min(nums2)

        if min1 < min2:
            return min1 * 10 + min2
        else:
            return min2 * 10 + min1