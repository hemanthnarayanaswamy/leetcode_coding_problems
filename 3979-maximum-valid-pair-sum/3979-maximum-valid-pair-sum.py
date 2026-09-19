class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        total = 0
        n = len(nums)
        maxTracker = [0]*n

        for i in range(n-1, -1, -1):
            if i == n-1:
                maxTracker[i] = nums[i]
            else:
                maxTracker[i] = max(maxTracker[i+1], nums[i])

        for i in range(n-k):
            total = max(total, nums[i]+maxTracker[i+k])
            
        return total