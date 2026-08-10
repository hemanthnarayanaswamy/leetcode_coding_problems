class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if nums.count(nums[0]) == len(nums):
            return 0
        else:
            return 1