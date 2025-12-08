class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = positive = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                positive = n - i
                break
            elif nums[i] < 0:
                negative += 1
        
        return max(negative, positive)