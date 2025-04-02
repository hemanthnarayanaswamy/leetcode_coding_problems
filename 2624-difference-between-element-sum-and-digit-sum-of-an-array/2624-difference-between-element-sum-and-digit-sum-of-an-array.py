class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_digits = sum(int(i) for i in ''.join([str(num) for num in nums]))

        return abs(sum_digits - sum(nums))
        