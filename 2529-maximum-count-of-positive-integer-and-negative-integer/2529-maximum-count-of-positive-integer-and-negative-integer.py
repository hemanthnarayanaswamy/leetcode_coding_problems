class Solution:
    def upperBound(self, nums):
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m
        
        return l
    
    def lowerBound(self, nums):
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m
        
        return l
        
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        print(self.upperBound(nums), self.lowerBound(nums))
        positive = n - self.upperBound(nums)
        negative = self.lowerBound(nums)
        
        return max(positive, negative)
        
