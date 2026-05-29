class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            nums[i] = total
            
        return min(nums)