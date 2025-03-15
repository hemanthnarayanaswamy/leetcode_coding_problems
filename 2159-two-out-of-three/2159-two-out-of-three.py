class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        for i in nums1:
            if i in nums2 or i in nums3:
                s.add(i)
        for j in nums2:
            if j in nums3:
                s.add(j)
        return list(s)