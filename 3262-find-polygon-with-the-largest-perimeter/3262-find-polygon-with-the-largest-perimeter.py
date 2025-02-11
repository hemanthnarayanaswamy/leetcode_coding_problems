class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] < sum(nums[i+1:len(nums)]):
                return sum(nums[i: len(nums)])
        return -1
        