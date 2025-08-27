class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
    
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        minPrefix = min(prefixSum)
        
        return max(1, 1 - minPrefix)
            