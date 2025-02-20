class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)

        if len(sorted_nums) < 3:
            return max(nums)
            
        return sorted_nums[2]
