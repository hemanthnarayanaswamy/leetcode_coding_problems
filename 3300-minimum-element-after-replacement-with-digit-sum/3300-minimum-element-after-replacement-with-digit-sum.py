class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            nums[i] = sum
            
        return min(nums)