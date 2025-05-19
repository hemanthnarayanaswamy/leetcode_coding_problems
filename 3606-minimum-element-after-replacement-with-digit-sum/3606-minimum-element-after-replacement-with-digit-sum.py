class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n

        for i in range(n):
            if nums[i] < 10:
                digitSum[i] = nums[i]
            else:
                digitSum[i] = sum([int(num) for num in str(nums[i])])
        
        return min(digitSum)
