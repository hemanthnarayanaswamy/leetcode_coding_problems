class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        left = 0
        currentSum = 0
        seen = set()

        for right in range(len(nums)):
            num = nums[right]
            while num in seen:
                numx = nums[left]
                seen.remove(numx)
                currentSum -= numx
                left += 1
            
            currentSum += num
            seen.add(num)
            maxSum = max(maxSum, currentSum)
        
        return maxSum
