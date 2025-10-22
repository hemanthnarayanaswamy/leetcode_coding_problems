class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = len(nums)
        totalSum = 0

        if sum(nums) < target:
            return 0

        for i in range(len(nums)):
            totalSum += nums[i]

            while totalSum >= target:
                totalSum -= nums[left]
                left += 1
                minLen = min(minLen, i+1 - (left-1))
        
        return minLen

