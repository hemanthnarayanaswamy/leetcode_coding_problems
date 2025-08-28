class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if i % 2: 
                should_be_peak = True
            else:
                should_be_peak = False
            
            a, b = nums[i], nums[i-1]
            
            if should_be_peak and a > b:
                continue
            elif not should_be_peak and a < b:
                continue
            else:
                    nums[i] = b
                    nums[i-1] = a
        
        return nums
        
