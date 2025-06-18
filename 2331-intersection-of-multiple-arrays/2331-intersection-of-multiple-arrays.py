class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        intersection_nums = set(nums[0])
        for i in range(1, len(nums)):
            intersection_nums &= set(nums[i])
        return sorted(intersection_nums)