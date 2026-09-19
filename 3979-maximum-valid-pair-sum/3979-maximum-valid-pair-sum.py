class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_total = 0
        suffix_max = nums[-1]

        # Iterate backward from the last valid index for i
        for i in range(n - k - 1, -1, -1):
            # Update suffix_max to include the valid choice at index i + k
            suffix_max = max(suffix_max, nums[i + k])
            max_total = max(max_total, nums[i] + suffix_max)

        return max_total