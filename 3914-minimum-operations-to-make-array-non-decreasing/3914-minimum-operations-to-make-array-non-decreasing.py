class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total = 0

        for i in range(1, len(nums)):
            d = nums[i-1] - nums[i]
            if d > 0:
                total += d
        
        return total 