class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n

        for i in range(n):
            digitSum[i] = sum([int(num) for num in str(nums[i])])
        
        return min(digitSum)
