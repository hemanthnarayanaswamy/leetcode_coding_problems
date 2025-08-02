class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        totalSum = sum(nums)
        currentSum = 0

        for i in range(len(nums)):
            if currentSum > totalSum:
                return nums[:i]
            else:
                totalSum -= nums[i]
                currentSum += nums[i]
        
        return nums

