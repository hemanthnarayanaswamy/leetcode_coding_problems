class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)

        if n <= 1:
            return 0

        for i in range(1,n):
            current, previous = nums[i], nums[i-1]
            diff = previous - current 

            if diff >= 0:
                nums[i] += diff+1
                operations += diff+1
        
        return operations
            


