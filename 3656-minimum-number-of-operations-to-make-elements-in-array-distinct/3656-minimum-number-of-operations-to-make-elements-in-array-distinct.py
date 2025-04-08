class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        operations = 0
        while i < n:
            if len(nums[i:]) == len(set(nums[i:])):
                return operations
            else:
                i += 3
                operations += 1

        return operations
        


        