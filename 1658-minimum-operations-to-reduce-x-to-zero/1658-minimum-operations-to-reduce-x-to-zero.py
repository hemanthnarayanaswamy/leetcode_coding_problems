class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        numSum = sum(nums)

        if numSum < x:
            return -1
        
        if numSum == x:
            return n

        target = numSum - x
        left = prefixSum = subLen = 0

        for right in range(len(nums)):
            prefixSum += nums[right]
            
            while prefixSum > target:
                prefixSum -= nums[left]
                left += 1
            
            if prefixSum == target:
                subLen = max(subLen, right - left + 1)
        
        return (n - subLen) if subLen else -1
