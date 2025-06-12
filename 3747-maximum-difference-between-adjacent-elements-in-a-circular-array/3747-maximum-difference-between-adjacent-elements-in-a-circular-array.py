class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        
        return max(abs(nums[i-1] - nums[i]) for i in range(1, len(nums)))