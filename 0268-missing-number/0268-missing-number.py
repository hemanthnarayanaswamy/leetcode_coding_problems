class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1) // 2
        nums_sum = sum(nums)

        return total_sum - nums_sum
        