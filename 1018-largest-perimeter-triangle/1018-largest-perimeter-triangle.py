class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return  nums[i+1] + nums[i+2] + nums[i]
            else:
                continue
        return 0