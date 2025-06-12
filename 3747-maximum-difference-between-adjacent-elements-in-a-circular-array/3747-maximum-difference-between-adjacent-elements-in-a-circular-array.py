class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            result = max(result, abs(nums[i-1] - nums[i]))
        
        return max(result, abs(nums[i] - nums[0]))