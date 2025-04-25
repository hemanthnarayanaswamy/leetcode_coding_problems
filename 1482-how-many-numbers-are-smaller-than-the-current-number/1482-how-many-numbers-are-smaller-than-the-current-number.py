class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        result = [0]*len(nums)

        for i in range(len(nums)): 
            result[i] = nums_sorted.index(nums[i])

        return result
