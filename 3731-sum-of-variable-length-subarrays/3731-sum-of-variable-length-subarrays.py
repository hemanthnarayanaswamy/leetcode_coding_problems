class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        
        for i, num in enumerate(nums):
            start = max(0, i - num)
            # Calculate sum from start to i
            subarray_sum = sum(nums[start:i+1])
            res += subarray_sum
        
        return res


