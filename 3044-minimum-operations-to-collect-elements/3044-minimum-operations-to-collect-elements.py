class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        collected = set()
        
        for i in range(len(nums) - 1, -1, -1):
            operations += 1
            
            # If we found one of our target numbers
            if 1 <= nums[i] <= k:
                collected.add(nums[i])
            
            # Check if we have collected all numbers from 1 to k
            if len(collected) == k:
                return operations
