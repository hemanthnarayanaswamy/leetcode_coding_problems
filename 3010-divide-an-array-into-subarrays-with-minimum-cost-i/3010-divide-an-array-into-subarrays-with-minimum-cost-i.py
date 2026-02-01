class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        new = nums[1:]
        new.sort()

        return nums[0] + new[0] + new[1]
        