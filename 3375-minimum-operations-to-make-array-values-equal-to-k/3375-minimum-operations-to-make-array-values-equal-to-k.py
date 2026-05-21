class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums), reverse=True)
        
        if min(nums) < k:
            return -1
        
        operations = 0 
        for num in nums:
            if num != k:
                operations += 1
            else:
                break
        
        return operations
