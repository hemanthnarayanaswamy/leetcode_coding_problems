class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            should_be_peak = False
            if i % 2: should_be_peak = True
            
            a, b = nums[i], nums[i-1]
            
            if should_be_peak and a < b or not should_be_peak and a > b:
                    nums[i] = b
                    nums[i-1] = a
        
        return nums
        
