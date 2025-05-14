class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # incrementing (n - 1) elements == decrementing 1 element
        # num steps to increase all to same element == num steps to decrease to min element
        return sum(nums) - len(nums) * min(nums)