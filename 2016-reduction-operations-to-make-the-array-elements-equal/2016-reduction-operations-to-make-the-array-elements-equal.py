class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        opperations = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                opperations += i
        return opperations
        