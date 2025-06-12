class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int: 
        N = len(nums) # REmains unchanges after appending, that way we can avoid the out of index range
        nums.append(nums[0])
        
        return max(abs(nums[i] - nums[i+1]) for i in range(N))