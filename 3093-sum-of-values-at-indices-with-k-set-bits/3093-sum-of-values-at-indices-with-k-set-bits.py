class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for i, num in enumerate(nums):
            if i.bit_count() == k:
                res += num
        
        return res