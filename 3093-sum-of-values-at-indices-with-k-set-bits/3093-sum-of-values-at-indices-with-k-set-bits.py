class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for i, num in enumerate(nums):
            if bin(i).count('1') == k:
                print(num)
                res += num
        
        return res