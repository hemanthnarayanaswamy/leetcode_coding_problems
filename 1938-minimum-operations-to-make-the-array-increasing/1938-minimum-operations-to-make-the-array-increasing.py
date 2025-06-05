class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1,len(nums)):
            current, previous = nums[i], nums[i-1]

            if current <= previous:
                nums[i] = previous + 1
                operations += previous - current + 1
        
        return operations
            


