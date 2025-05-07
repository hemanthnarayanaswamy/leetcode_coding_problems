class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations = 0
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                operations += i+1
        
        return operations

        