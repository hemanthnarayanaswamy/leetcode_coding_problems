class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return max([nums[i] + nums[n - 1 - i] for i in range(n // 2)])