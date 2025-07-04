class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        NEG_INF = float('-inf')
        
        for i, v in enumerate(nums):
            left  = nums[i-k] if i - k >= 0   else NEG_INF
            right = nums[i+k] if i + k < n    else NEG_INF
            
            if v > left and v > right:
                total += v
        
        return total
