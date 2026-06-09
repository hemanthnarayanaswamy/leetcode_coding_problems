class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        num_max = max(nums)
        num_min = min(nums)

        return k * (num_max - num_min)