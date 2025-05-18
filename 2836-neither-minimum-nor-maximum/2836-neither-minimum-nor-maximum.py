class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 <= n <= 2:
            return -1 

        nums = sorted(nums)

        return nums[1]
        