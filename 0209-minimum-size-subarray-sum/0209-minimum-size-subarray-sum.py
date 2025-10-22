class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float('inf')
        totalSum = 0

        for i in range(len(nums)):
            totalSum += nums[i]

            while totalSum >= target:
                totalSum -= nums[left]
                minLen = min(minLen, i+1-left)
                left += 1
                
        return 0 if minLen == float('inf') else minLen
