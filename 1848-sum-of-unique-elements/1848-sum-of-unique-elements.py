class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums = Counter(nums)

        return sum([key for key, value in nums.items() if value == 1])