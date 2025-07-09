class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            right_sum = total_sum - left_sum
            left_sum += nums[i]
            # Check if left sum equals the right sum
            if left_sum == right_sum:
                return i

        return -1
        