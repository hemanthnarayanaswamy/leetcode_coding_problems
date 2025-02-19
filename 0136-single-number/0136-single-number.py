class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0000
        for num in nums:
            result ^= num 
        return result 

        