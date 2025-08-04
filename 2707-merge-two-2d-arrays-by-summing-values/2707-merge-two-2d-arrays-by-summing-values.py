class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        l1 = l2 = 0

        while l1 < len(nums1) and l2 < len(nums2):
            a, b = nums1[l1][0], nums1[l1][1]
            x, y = nums2[l2][0], nums2[l2][1]

            if a == x:
                res.append([a, b+y])
                l1 += 1
                l2 += 1
            elif a < x:
                res.append([a, b])
                l1 += 1
            else: 
                res.append([x, y])
                l2 += 1
        
        if l1 < len(nums1):
            res += nums1[l1:]
        elif l2 < len(nums2):
            res += nums2[l2:]
        
        return res

