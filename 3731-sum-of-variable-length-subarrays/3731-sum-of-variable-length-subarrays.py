class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        prefix_sum = [0]
        
        # Build prefix sum array
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        for i, num in enumerate(nums):
            start = max(0, i - num)
            # Sum from start to i using prefix sums
            subarray_sum = prefix_sum[i + 1] - prefix_sum[start]
            res += subarray_sum
        
        return res

