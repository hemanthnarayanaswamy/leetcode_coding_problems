class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = (max(nums) - k) - (min(nums) + k)
        return max(0, diff)