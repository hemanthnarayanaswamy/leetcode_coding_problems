class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        p1, p2 = nums[:2]
        maxFib = fib = 2

        for i in range(2, n):
            if p1 + p2 == nums[i]:
                fib += 1
                maxFib = max(maxFib, fib)
            else:
                fib = 2
            
            p1, p2 = p2, nums[i]
            
        return maxFib
                
        
