class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()

        return sum(nums[-2:]) - nums[0]
        