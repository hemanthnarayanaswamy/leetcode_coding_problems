class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            should_be_peak = False
            if i % 2: should_be_peak = True
            
            if should_be_peak and nums[i] < nums[i-1] or not should_be_peak and nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums
        
