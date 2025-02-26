class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0 
        
        nums = sorted(nums)
        min_result = nums[k-1] - nums[0]  ## Calculate the differennce between max and min in the first sub array

        for i in range(k, len(nums)):
            min_result = min(min_result, nums[i] - nums[i-k+1])

        return min_result
        