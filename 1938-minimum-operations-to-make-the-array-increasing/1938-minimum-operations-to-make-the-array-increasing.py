class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1,len(nums)):
            current, previous = nums[i], nums[i-1]

            if current <= previous:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                operations += increment 
        
        return operations
            


