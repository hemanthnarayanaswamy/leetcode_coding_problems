class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        n = 1 

        while n*k in nums:
            n += 1
        
        return n * k