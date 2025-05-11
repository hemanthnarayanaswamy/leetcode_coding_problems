class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        goodCounter = 0 

        for n in nums1:
            for m in nums2:
                if n % (m * k)  == 0:
                    goodCounter += 1
        
        return goodCounter 