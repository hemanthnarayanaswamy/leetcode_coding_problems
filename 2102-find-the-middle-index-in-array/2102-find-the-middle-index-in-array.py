class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)      
        left_sum = 0           
        
        for i, x in enumerate(nums):
            # total − left_sum − x == sum of elements to the right of i
            if left_sum == total - left_sum - x:
                return i
            left_sum += x       # include nums[i] for the next iteration
        
        return -1               # no such index found
